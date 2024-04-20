from django.shortcuts import render
from django.http import JsonResponse
from .models import *

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
        # Obtener todas las ciudades asociadas al país 
        
        cargos = Cartarvue.objects.filter(aeronave=id_aeronave).values()
        for cargo in cargos:
            id_cargo = cargo['cargo']
            nombre_cargo = Caratenvue.objects.get(cargo=id_cargo).nombre
            cargo['nombre_cargo'] = nombre_cargo
        cargos_list = list(cargos) 
        # Devolver los datos como JSON
        return JsonResponse(cargos_list, safe=False)
    except Cartarvue.DoesNotExist:
        # Manejar el caso en el que el país no exista
        return JsonResponse({'error': 'No Existen tarifas'}, status=404)

def cargos_manejo(request): 
    if request.method == "GET":
        cargos = Cargcaman.objects.all().values()
        try:      
            for cargo in cargos:
                if cargo['naturaleza'] != None:   
                    id_naturaleza = cargo['naturaleza']
                    nom_naturaleza = Carnatur.objects.get(naturaleza=id_naturaleza).nombre
                    cargo['nom_naturaleza'] = nom_naturaleza
            cargos_list = list(cargos)
            return JsonResponse(cargos_list, safe=False)
        
        except Cargcaman.DoesNotExist:
            return JsonResponse({'error': 'No se encontraron Cargos de Mantenimiento'}, status=404)

def tarifas_manejo(request):
    id_cargo = request.GET.get('id_cargo')  # Obtener el valor del parámetro id_pais de la URL  
    try:
        # Obtener el país con el ID proporcionado
        # Obtener todas las ciudades asociadas al país
        cargos = Cartarman.objects.filter(tarifa='01', cargo=id_cargo ) 
        for cargo in cargos:
            if cargo['aplica'] == 'P':
                nom_aplica = 'Peso'
            else:
                nom_aplica ='Volumen'    
        cargo_list = list(cargos)

        # Devolver los datos como JSON
        return JsonResponse(cargo_list, safe=False)
    except Cartarman.DoesNotExist:
        # Manejar el caso en el que el país no exista
        return JsonResponse({'error': 'No se encontraron Tarifas'}, status=404)