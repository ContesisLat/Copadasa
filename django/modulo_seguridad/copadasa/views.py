from django.shortcuts import render
from django.http import JsonResponse
from .models import *

def naturaleza_cargos(request):
    if request.method == "GET":
        naturaleza = Carnatur.objects.all().values()
        try:
            for natur in naturaleza:
                if natur['status'] == "A":
                    natur['nom_status'] = "Activo"
                else:
                    natur['nom_status'] = "Inactivo"
                if natur['cargo'] != None:
                    id_cargo = natur['cargo']
                    nom_cargo = Cargcaman.objects.get(cargo=id_cargo).nombre
                    natur['nom_cargo'] = nom_cargo
                
            naturaleza_list = list(naturaleza)
            return JsonResponse(naturaleza_list, safe=False)
        except Carnatur.DoesNotExist:
            return JsonResponse({'Error': 'No pudo cargar Naturalezas'}, status=404)


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
    
def cargos_aereos(request):
    print('ingreso')
    if request.method == "GET":
        cargos = Caratenvue.objects.all().values()
        try:
            for cargo in cargos:
                if cargo['status'] == "A":
                    cargo['nom_status'] = "Activo"
                else:
                    cargo['nom_status'] = "Inactivo"

            cargos_list = list(cargos)
            return JsonResponse(cargos_list, safe=False)
        except Caratenvue.DoesNotExist:
            return JsonResponse({'error': 'No Existen Cargos'}, status=404)

def tarifas_aeronaves(request):
    id_aeronave = request.GET.get('id_aeronave')  # Obtener el valor del parámetro id_aeronave de la URL
    try:
        # Obtener el país con el ID proporcionado
        # Obtener todas las ciudades asociadas al país 
        tipos = Cartiaero.objects.all().values()
        for tipo in tipos:
            if tipo['status'] == "A":
                tipo['nom_status'] = "Activo"
            else:
                tipo['nom_status'] = "Inactivo"

        cargos = Cartarvue.objects.filter(aeronave=id_aeronave).values()
        for cargo in cargos:
            if cargo['status'] == "A":
                cargo['nom_status'] = "Activo"
            else:
                cargo['nom_status'] = "Inactivo"

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
                if cargo['status'] == 'A':
                    cargo['nom_status'] = "Activo"
                else:
                    cargo['nom_status'] = "Inactivo"

            cargos_list = list(cargos)
            return JsonResponse(cargos_list, safe=False)
        
        except Cargcaman.DoesNotExist:
            return JsonResponse({'error': 'No se encontraron Cargos de Mantenimiento'}, status=404)

def tarifas_manejo(request):
    id_cargo = request.GET.get('id_cargo')  # Obtener el valor del parámetro id_pais de la URL
    id_tarifa = request.GET.get('id_tarifa')
    try:
        # Obtener el país con el ID proporcionado
        # Obtener todas las ciudades asociadas al país
        cargos = Cartarman.objects.filter(tarifa=id_tarifa, cargo=id_cargo).values()
        for cargo in cargos:
            if cargo['status'] == 'A':
                cargo['nom_status'] = 'Activo'
            else:
                cargo['nom_status'] = 'Inactivo'

            if cargo['aplica'] == 'P':
                cargo['nom_aplica'] = 'Peso'
            if cargo['aplica'] == 'V':
                cargo['nom_aplica'] = 'Volumen'
            if cargo['aplica'] == 'G':
                cargo['nom_aplica'] = 'General'
                    
        cargo_list = list(cargos)

        # Devolver los datos como JSON
        return JsonResponse(cargo_list, safe=False)
    except Cartarman.DoesNotExist:
        # Manejar el caso en el que el país no exista
        return JsonResponse({'error': 'No se encontraron Tarifas'}, status=404)
    
def tarifas_almacenaje(request):
    try:
        if request.method == "GET":
            id_tarifa = "01"
            tarifas = Cartaralm.objects.all().values()
            for tarifa in tarifas:
                if tarifa['status'] == "A":
                    tarifa['nom_status'] = "Activo"
                else:
                    tarifa['nom_status'] = "Inactivo"

            tarifa_list = list(tarifas)
            return JsonResponse(tarifa_list, safe=False)
    except Cartaralm.DoesNotExist:
        return JsonResponse({'error': 'No puede accesar Tarifas'}, status=404 )
          
def tarifas_frio(request):
    if request.method == "GET":
        try:
            id_tarifa = "03"
            tarifas = Cartari.objects.filter(tarifa=id_tarifa).values()
            for tarifa in tarifas:
                if tarifa['status'] == "A":
                    tarifa['nom_status'] = "Activo"
                else:
                    tarifa['nom_status'] = "Inactivo"
            
            lista_tarifa = list(tarifas)
            return JsonResponse(lista_tarifa, safe=False)
        except Cartari.DoesNotExist:
            return JsonResponse({'error': 'Error al cargar Tarifas'}, status=404)