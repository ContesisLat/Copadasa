from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import SegUser
import json

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
