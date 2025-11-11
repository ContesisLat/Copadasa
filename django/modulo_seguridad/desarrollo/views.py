from django.http import JsonResponse 
from django.views.decorators.csrf import csrf_exempt
from .models import SegUser
import json
from django.core.mail import EmailMessage
from django.views import View
from django.utils.decorators import method_decorator
from rest_framework.decorators import api_view
from django.conf import settings
from PIL import Image
from django.db import connection
from pyzbar.pyzbar import decode
from rest_framework import generics
from .serializer import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from django.db import connections

# Create your views here.

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        nombre_usuario = data.get('nombre_usuario','')
        contrasena = data.get('contrasena','')
        
        #buscar el usuario en la base de datos 
        try:
            user = SegUser.objects.get(nombre_usuario=nombre_usuario)
        except SegUser.DoesNotExist:
            user = None

        #verificar contraseña
        if user is not None and user.contrasena == contrasena:
            return JsonResponse({'message':'Autenticacion exitosa'})
        else:
            return JsonResponse({'message':'Credenciales invalidas'},status=401)
        
    return JsonResponse({'message':request.method},status=405)

@api_view(['POST'])
def obtener_programas_y_subprogramas(request):
    perfil = request.data.get('perfil')  # viene desde Vue

    if not perfil:
        return Response({"error": "Falta el perfil"}, status=400)

    with connections['default'].cursor() as cursor:
        # Obtener solo los programas que tengan subprogramas para el perfil dado
        cursor.execute("""
            SELECT DISTINCT p.proceso, p.descripcion
            FROM segproc p
            JOIN segpape s ON p.proceso = s.proceso
            WHERE s.perfil = %s
            ORDER BY p.descripcion
        """, [perfil])
        programas = cursor.fetchall()  # [(proceso, descripcion), ...]

        resultado = []

        for proceso, descripcion in programas:
            # Obtener los subprogramas correspondientes a ese proceso y perfil
            cursor.execute("""
                SELECT s.programa
                FROM segpape s
                WHERE s.proceso = %s AND s.perfil = %s
                ORDER BY s.programa
            """, [proceso, perfil])

            subprogramas = cursor.fetchall()  # [(nombre_subprograma,), ...]

            # Solo añadimos si hay subprogramas (seguridad extra)
            if subprogramas:
                resultado.append({
                    "proceso": descripcion,
                    "subprogramas": [{"programa": s[0]} for s in subprogramas]
                })

    return Response(resultado)

@method_decorator(csrf_exempt, name='dispatch')
class EnviarCorreoView(View):
    def post(self, request):
        # Obtener los datos del formulario (correo, mensaje, archivo)
        correo_remitente = request.POST.get('correo_remitente')
        mensaje = request.POST.get('mensaje')
        archivo = request.FILES.get('archivo')  # Obtiene el archivo adjunto si existe
        
        if correo_remitente and mensaje:
            # Crear el correo electrónico
            email = EmailMessage(
                subject="Copadasa",
                body=mensaje,
                from_email=settings.EMAIL_HOST_USER,
                to=['contesispty@gmail.com'],  # Cambia esto por el correo destino
                reply_to=[correo_remitente],  # Opción para responder al remitente
            )

            # Adjuntar archivo si existe
            if archivo:
                email.attach(archivo.name, archivo.read(), archivo.content_type)
            
            try:
                # Enviar el correo
                email.send()
                return JsonResponse({'status': 'success', 'message': 'Correo enviado correctamente'})
            except Exception as e:
                return JsonResponse({'status': 'error', 'message': str(e)})
        else:
            return JsonResponse({'status': 'error', 'message': 'Correo o mensaje no proporcionado'})
        

@api_view(['POST'])
def barcode_reader(request):
    try:
        # Obtener la imagen enviada desde el frontend
        image_file = request.FILES.get('barcode_image')
        
        if not image_file:
            return JsonResponse({'error': 'no se proporciono ningun archivo'}, status=400)

        # Leer la imagen utilizando PIL
        image = Image.open(image_file)

        # Decodificar el código de barras en la imagen
        decoded_objects = decode(image)

        # Si no se encontró ningún código de barras, retornar un error
        if not decoded_objects:
            return JsonResponse({'error': 'No se detecta codigo de barras en la imagen'}, status=400)

        # Extraer la información del código de barras (puede haber más de uno, tomamos el primero)
        barcode_data = decoded_objects[0].data.decode('utf-8')
        barcode_type = decoded_objects[0].type

        # Responder con los datos obtenidos
        return JsonResponse({
            'barcode_data': barcode_data,
            'barcode_type': barcode_type
        })

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
@api_view(['POST'])
def query_global(request):
    try:
        # Decodificar el cuerpo de la solicitud para obtener los datos JSON
        data = json.loads(request.body)

        tabla = data.get('tabla')
        filtro = data.get('filtro', {})

        if not tabla:
            return JsonResponse({'error': "Falta el parámetro 'tabla'"}, status=400)

        # Validación: asegúrate de que no haya filtros vacíos en el diccionario
        filtro = {key: value for key, value in filtro.items() if value}  # Elimina claves con valores vacíos

        # Construir la cláusula WHERE de la consulta SQL
        where_clauses = []
        params = []
        for key, value in filtro.items():
            where_clauses.append(f"{key} = %s")
            params.append(value)

        # Construir la consulta SQL dinámica
        sql_query = f"SELECT * FROM {tabla}"
        if where_clauses:
            sql_query += " WHERE " + " AND ".join(where_clauses)

        # Ejecutar la consulta SQL
        with connection.cursor() as cursor:
            cursor.execute(sql_query, params)
            columns = [col[0] for col in cursor.description]
            results = [dict(zip(columns, row)) for row in cursor.fetchall()]

        # Retornar los resultados como JSON
        return JsonResponse(results, safe=False)

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Error al decodificar los datos JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
    

class SegUserFilterView(generics.ListAPIView):
    queryset = SegUser.objects.all()
    serializer_class = SegUserSerializer
    filter_backends = [DjangoFilterBackend]  
    filterset_fields = ['nombre_usuario']  