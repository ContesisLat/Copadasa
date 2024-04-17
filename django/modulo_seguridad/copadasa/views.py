from django.shortcuts import render
from django.http import JsonResponse
from .models import Ciudades, Paises,Puertos, Cartiaero, Caratenvue, \
                    Cartarvue, Cartitar, Cargcaman, Cartarman

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
    
def tarifas_aeronaves(request):
    id_aeronave = request.GET.get('id_aeronave')  # Obtener el valor del parámetro id_aeronave de la URL
    try:
        # Obtener el país con el ID proporcionado
        nombre_aero = Cartiaero.objects.get(aeronave=id_aeronave).descripcion
        # Obtener todas las ciudades asociadas al país
        cargos = Cartarvue.objects.get(aeronave=id_aeronave).values()
        for cargo in cargos:
            nombre_cargo = Caratenvue.objects.get(cargo=cargos.cargo).nombre
            cargo['nombre_taeronave'] = nombre_aero
            cargo['nombre_cargo'] = nombre_cargo
        cargos_list = list(cargos) 
        # Devolver los datos como JSON
        return JsonResponse(cargos_list, safe=False)
    except Cartarvue.DoesNotExist:
        # Manejar el caso en el que el país no exista
        return JsonResponse({'error': 'No Existen tarifas'}, status=404)
    
def tarifa_manejo(request):
    id_tarifa = request.GET.get('id_tarifa')  # Obtener el valor del parámetro id_pais de la URL
    id_cargo = request.Get.get('id_cargo')
    try:
        # Obtener el país con el ID proporcionado
        nom_tarifa = Cartitar.objects.get(tarifa=id_tarifa).nombre
        nom_cargo = Cargcaman.objects.get(cargo=id_cargo).nombre
        # Obtener todas las ciudades asociadas al país
        tarifas = Cartarman.objects.filter(tarifa=id_tarifa).values()
        for tarifa in tarifas:
            tarifa['nombre_tarifa'] = nom_tarifa
            tarifa['nombre_cargo'] = nom_cargo
        tarifa_list = list(tarifas) 
        # Devolver los datos como JSON
        return JsonResponse(tarifa_list, safe=False)
    except Paises.DoesNotExist:
        # Manejar el caso en el que el país no exista
        return JsonResponse({'error': 'No se encontraron Tarifas'}, status=404)