from django.shortcuts import render
from .models import Ciudades, Paises,Puertos
from django.http import JsonResponse

def ciudades_por_pais(request):
    id_pais = request.GET.get('id_pais')  # Obtener el valor del parámetro id_pais de la URL
    try:
        # Obtener el país con el ID proporcionado
        nombre_pais = Paises.objects.get(pais=id_pais).nombre
        # Obtener todas las ciudades asociadas al país
        ciudades = Ciudades.objects.filter(pais=id_pais).values()
        for ciudad in ciudades:
            ciudad['nombre_pais'] = nombre_pais
        ciudades_list = list(ciudades) 
        # Devolver los datos como JSON
        return JsonResponse(ciudades_list, safe=False)
    except Paises.DoesNotExist:
        # Manejar el caso en el que el país no exista
        return JsonResponse({'error': 'El país no existe'}, status=404)

def puertos_por_pais(request):
    id_ciudad = request.GET.get('id_ciudad')
    id_pais = request.GET.get('id_pais')
    try:
        nombre_ciudad = Ciudades.objects.get(ciudad=id_ciudad,pais=id_pais).nombre
        nombre_pais = Paises.objects.get(pais=id_pais).nombre
        puertos = Puertos.objects.filter(ciudad=id_ciudad,pais=id_pais).values()
        for puerto in puertos:
            puerto['nombre_ciudad'] = nombre_ciudad
            puerto['nombre_pais'] = nombre_pais
        puertos_list = list(puertos)
        return JsonResponse(puertos_list, safe=False)
    except Paises.DoesNotExist:
        return JsonResponse({'error': 'El país no existe'}, status=404)