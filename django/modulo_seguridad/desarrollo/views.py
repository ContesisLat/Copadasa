from django.http import JsonResponse 
from django.views.decorators.csrf import csrf_exempt
from .models import SegUser
import json
from django.core.mail import EmailMessage
from django.views import View
from django.utils.decorators import method_decorator
from django.conf import settings
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