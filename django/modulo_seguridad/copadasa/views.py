import json
from django.db import connection, connections
from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import generics
from .serializer import *
from django_filters.rest_framework import DjangoFilterBackend

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
        with connections['copadasa_db'].cursor() as cursor:
            cursor.execute(sql_query, params)
            columns = [col[0] for col in cursor.description]
            results = [dict(zip(columns, row)) for row in cursor.fetchall()]

        # Retornar los resultados como JSON
        return JsonResponse(results, safe=False)

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Error al decodificar los datos JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
    
    return JsonResponse({'error': 'Método no permitido'}, status=405)


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
    
def anaqueles_por_area(request):
    if request.method == "GET":
        id_almacen = request.GET.get('id_almacen')
        id_area = request.GET.get('id_area')
        loganaquel = Loganaquel.objects.filter(almacen=id_almacen, area=id_area).values()
        try:
            for anaquel in loganaquel:
                if anaquel['status'] == "A":
                    anaquel['nom_status'] = "Activo"
                else:
                    anaquel['nom_status'] = "Inactivo"

            loganaquel_list = list(loganaquel) 
            return JsonResponse(loganaquel_list, safe=False)
        except Loganaquel.DoesNotExist:
            return JsonResponse({'Error': 'No se pudo cargar los Anaqueles'}, status=404)

def anaqueles_por_ubicacion(request):
    if request.method == "GET":
        id_almacen = request.GET.get('id_almacen')
        id_area = request.GET.get('id_area')
        id_anaquel = request.GET.get('id_anaquel')
        id_cara = request.GET.get('id_cara')
        logubica = Logubica.objects.filter(almacen=id_almacen, area=id_area, anaquel=id_anaquel, cara=id_cara).values()
        try:
            for ubica in logubica:
                if ubica['status'] == "A":
                    ubica['nom_status'] = "Activo"
                else:
                    ubica['nom_status'] = "Inactivo"
        
            logubica_list = list(logubica)
            return JsonResponse(logubica_list, safe=False)
        except Logubica.DoesNotExist:
            return JsonResponse({'Error': 'No se pudo cargar las ubicaciones'}, status=404)
        
def areas_de_bodega(request):
    logarea = Logarea.objects.all().values()
    try:
        for area in logarea:
            id_almacen = area['almacen']
            nombre = Logalma.objects.get(almacen =id_almacen).descripcion
            area['nom_almacen'] = nombre

            if area['status'] == "A":
                area['nom_status'] = "Activo"
            else:
                area['nom_status'] = "Inactivo"

        area_list = list(logarea)
        return JsonResponse(area_list, safe=False)
    except Logalma.DoesNotExist:
        return JsonResponse({'error': 'Almacen no existe'}, status=404)


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
        
def control_manifiestos(request):
    if request.method == "GET":
        manifiesto = Carcmani.objects.all().values()
        try:
            for man in manifiesto:
                id_operador = man['operador']
                id_puerto = man['puerto_despacho']
                nom_puerto = Puertos.objects.get(puerto=id_puerto).nombre
                man['nom_pto_despacho'] = nom_puerto

                id_puerto = man['puerto_destino']
                nom_puerto = Puertos.objects.get(puerto=id_puerto).nombre
                man['nom_pto_destino'] = nom_puerto

                nom_operador = Caropera.objects.get(operador=id_operador).nombre
                man['nom_operador'] = nom_operador

                id_aeronave = man['aeronave']
                nom_aeronave = Cartiaero.objects.get(aeronave=id_aeronave).descripcion
                man['nom_aeronave'] = nom_aeronave

                if man['status'] == "A":
                    man['nom_status'] = "Activo"
                else:
                    man['nom_status'] = "Inactivo"

            manifiesto_list = list(manifiesto)
            return JsonResponse(manifiesto_list, safe=False)
        except Carcmani.DoesNotExist:
            return JsonResponse({'error': 'No Existen Manifiestos'}, status=404)


def tarifas_aeronaves(request):
    id_aeronave = request.GET.get('id_aeronave')  # Obtener el valor del parámetro id_aeronave de la URL
    try:
        # Obtener el país con el ID proporcionado
        # Obtener todas las ciudades asociadas al país 

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

def indicadores_carga(request):
    if request.method == "GET":
        indicador = Carinent.objects.all().values()
        try:
            for indi in indicador:
                if indi['tipo'] == 'E':
                    indi['nom_tipo'] = "Entrega"

                if indi['status'] == 'A':
                    indi['nom_status'] = "Activo"
                else:
                    indi['nom_status'] = "Inactivo"
                
            indicador_list = list(indicador)
            return JsonResponse(indicador_list, safe=False)
        except Carinent.DoesNotExist:
            return JsonResponse({'error': 'No Existen Indicadores'}, status=404)
        
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


#nuevo filtrado en tabla        
class CardmaniFilterView(generics.ListAPIView):
    queryset = Cardmani.objects.all()
    serializer_class = CardmaniSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['numero_vuelo']  # Aquí defines los campos por los que quieres filtrar

class PuertosFilterView(generics.ListAPIView):
    queryset = Cardmani.objects.all()
    serializer_class = PuertosSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status'] 