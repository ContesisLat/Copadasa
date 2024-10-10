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
import io
from pyzbar.pyzbar import decode
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