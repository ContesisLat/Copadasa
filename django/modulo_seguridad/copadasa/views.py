import base64
import json
import os
from django.db import connection, connections
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import *
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import generics
from .serializer import *
from django_filters.rest_framework import DjangoFilterBackend
import decimal
from django.db.models import Sum
from datetime import date, datetime,time, timedelta
from django.utils import timezone
#from django.db import transaction

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

@csrf_exempt
def guardar_archivos(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
 
            matricula_base64 = data.get('matricula')
            cedula_base64 = data.get('cedula')
            firma_base64 = data.get('firma')
            embarque= data.get('no_embarque')
            modificadopor = data.get('modificado_por')
            fechaS = data.get('fecha_status')
            horaS = data.get('hora_status')

            # Ruta base fija donde guardar
            ruta_base = r"/Copadasa"  # Cambia por la ruta real

            # Subcarpetas
            path_matricula = os.path.join(ruta_base, 'matriculas')
            path_cedula = os.path.join(ruta_base, 'cedulas')
            path_firma = os.path.join(ruta_base, 'firmas')

            # Crear carpetas si no existen
            os.makedirs(path_matricula, exist_ok=True)
            os.makedirs(path_cedula, exist_ok=True)
            os.makedirs(path_firma, exist_ok=True)

            # Timestamp único
            timestamp = timezone.localtime(timezone.now()).strftime("%Y-%m-%d-%H%M%S")

            # Guardar matrícula
            if matricula_base64 and "," in matricula_base64:
                data = base64.b64decode(matricula_base64.split(",")[1])
                final_pathM = os.path.join(path_matricula, f"matricula_{timestamp}.png")
                print(final_pathM)
                with open(final_pathM, "wb") as f:
                    f.write(data)

            # Guardar cédula
            if cedula_base64 and "," in cedula_base64:
                data = base64.b64decode(cedula_base64.split(",")[1])
                final_pathC = os.path.join(path_cedula, f"cedula_{timestamp}.png")
                with open(final_pathC, "wb") as f:
                    f.write(data)

            # Guardar firma
            if firma_base64 and "," in firma_base64:
                data = base64.b64decode(firma_base64.split(",")[1])
                final_pathF = os.path.join(path_firma, f"firma_{timestamp}.png")
                with open(final_pathF, "wb") as f:
                    f.write(data)
                    # Ahora final_path contiene la ruta completa del archivo

            Carentre.objects.filter(no_embarque=embarque).update(modificado_por=modificadopor, fecha_status = fechaS, hora_status = horaS, status = 'F', cedula = final_pathC,
                                                                 no_placa = final_pathM, firma_digital = final_pathF)
            return JsonResponse({"status": "ok", "mensaje": "Archivos guardados con éxito"})

        except Exception as e:
            import traceback
            print("ERROR al guardar archivos:", e)
            traceback.print_exc() 
            return JsonResponse({"status": "error", "mensaje": str(e)}, status=500)

    return JsonResponse({"status": "error", "mensaje": "Método no permitido"}, status=405)

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
        
def control_manifiesto(request):
    if request.method == "GET":
        manifiesto = Carcmani.objects.all().values() 
        try:
            for man in manifiesto:
                id_operador = man['operador'] 
                nom_operador = Caropera.objects.get(operador=id_operador).nombre
                man['nom_operador'] = nom_operador

                id_puertor = man['puerto_despacho']
                nom_puerto = Puertos.objects.get(puerto=id_puertor).nombre
                man['nom_pto_despacho'] = nom_puerto
                 
                id_puerto = man['puerto_destino']
                nom_puerto = Puertos.objects.get(puerto=id_puerto).nombre
                man['nom_pto_destino'] = nom_puerto
             
                id_aeronave = man['aeronave']            
                nom_aeronave = Cartiaero.objects.get(aeronave=id_aeronave).descripcion
                man['nom_aeronave'] = nom_aeronave

                if man['status'] == "R":
                    man['nom_status'] = "Registrado"
                if man['status'] == "C":
                    man['nom_status'] = "Confirmado"
                if man['status'] == "K":
                    man['nom_status'] = "Liquidado"
                if man['status'] == "D":
                    man['nom_status'] = "Despachado"
                if man['status'] == "E":
                    man['nom_status'] = "Anulado"
                

            manifiesto_list = list(manifiesto)
            return JsonResponse(manifiesto_list, safe=False)
        except Carcmani.DoesNotExist:      
            return JsonResponse({'error': 'No Existen Manifiestos'}, status=404)

def detalle_manifiesto(request):
    id_fecha = request.GET.get('id_fecha')
    id_operador = request.GET.get('id_operador')
    id_numero_vuelo = request.GET.get('id_numero_vuelo')

    cardmani = Cardmani.objects.filter(fecha=id_fecha, operador=id_operador, numero_vuelo=id_numero_vuelo).values()
    try:
        for dmani in cardmani:
            id_naturaleza = dmani['naturaleza']
            nombre_natur = Carnatur.objects.get(naturaleza=id_naturaleza).nombre
            dmani['nom_naturaleza'] = nombre_natur

            if dmani['status'] == "R":
                dmani['nom_status'] = "Registrado"
            if dmani['status'] == "L":
                dmani['nom_status'] = "Confirmado"
            if dmani['status'] == "C":
                dmani['nom_status'] = "Calculado"
            if dmani['status'] == "K":
                dmani['nom_status'] = "Liquidado"
            if dmani['status'] == "D":
                dmani['nom_status'] = "Despachado"

        cardmani_list = list(cardmani)
        return JsonResponse(cardmani_list, safe=False)
    except Cardmani.DoesNotExist:
        return JsonResponse({'Error:' 'No existen detalles detalles'}, status=404)

def compania_aerea(request):
    carcoaer = Carcoaer.objects.all().values()
    try:
        for comp in carcoaer:
            if comp['status'] == "A":
                comp['nom_status'] = "Activo"
            else:
                comp['nom_status'] = "Inactivo"
        
        carcoaer_list = list(carcoaer)
        return JsonResponse(carcoaer_list, safe=False)
    except Carcoaer.DoesNotExist:
        return JsonResponse({'error': 'No hay compañías'}, status=404)

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
        id_tarifa = request.GET.get('id_tarifa')
        try:
            #id_tarifa = "03"
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

def transacciones_almacen(request):
    logtral = Logtral.objects.all().values()
    try:
        for tral in logtral:
            if tral['status'] == "A":
                tral['nom_status'] = "Activo"
            else:
                tral['nom_status'] = "Inactivo"

            if tral['accion'] == "S":
                tral['nom_accion'] = "Suma"
            else:
                tral['nom_accion'] = "Resta"

            if tral['maneja_cliente'] == "S":
                tral['nom_maneja_clte'] = "Sí"
            else:
                tral['nom_maneja_clte'] = "No"

        logtral_list = list(logtral)
        return JsonResponse(logtral_list, safe=False)
    except Logtral.DoesNotExist:
        return JsonResponse({'Error': 'No hay información'}, status=404)    
    
def calcula_manifiesto(request):
        id_reg = request.GET.get('id')
        cardmani = Cardmani.objects.filter(id=id_reg).values()
        now = datetime.now()
        try:
            for detalle in cardmani:
                m_fecha = detalle['fecha']
                id_operador = detalle['operador']
                id_numero_vuelo = detalle['numero_vuelo']
                id_no_embarque = detalle['no_embarque']

                fecha_confirma = detalle['fecha_confirma']
                hora_confirma = detalle['hora_confirma']

                Cardeent.objects.filter(fecha_manifiesto=m_fecha, operador=id_operador, 
                                numero_vuelo=id_numero_vuelo, no_embarque=id_no_embarque).delete()
            
                Carentre.objects.filter(fecha_manifiesto=m_fecha, operador=id_operador, 
                                    numero_vuelo=id_numero_vuelo, no_embarque=id_no_embarque).delete()
            
                id_cant_items = detalle['cant_items']
                id_destinatario = detalle['destinatario']
                id_peso = detalle['peso_kg']
                id_fecha = now.date()
                w_hora = now.time()
                id_hora = w_hora.strftime('%H:%M:%S')
                Carentre.objects.create(fecha=id_fecha, fecha_manifiesto=m_fecha, operador=id_operador,
                                     numero_vuelo=id_numero_vuelo, no_embarque=id_no_embarque, creado_por='contesis',
                                     fecha_creado=id_fecha, hora_creado=id_hora, piezas_entrega=id_cant_items,
                                     piezas_faltantes=0, piezas_buenas=id_cant_items, monto=0, status='G', 
                                     destinatario=id_destinatario, peso=id_peso)
            
            #cargcaman = Cargcaman.objects.filter(tipo='M', status='A').values()
       
            #for cargo in cargcaman:
               
                tarifa = Cartitar.objects.get(tipo='M', status='A').tarifa
                cartarman = Cartarman.objects.filter(tarifa=tarifa, status='A').values()
                for tarifa in cartarman:
                    id_cargo = tarifa['cargo']
                    id_valor = tarifa['valor']
                    id_aplica = tarifa['aplica']
                    if id_aplica == 'G':
                        valor = id_valor
                    if id_aplica == 'P':
                        valor = id_valor * id_peso

                    Cardeent.objects.create(fecha=id_fecha, fecha_manifiesto=m_fecha, operador=id_operador,
                                        numero_vuelo=id_numero_vuelo, no_embarque=id_no_embarque, tarifa=id_cargo,
                                        monto= valor, status='A', fecha_status=id_fecha, hora_status=id_hora)
                    
                Cardmani.objects.filter(id=id_reg).update(status='C', modificado_por='contesis', 
                                            fecha_status=id_fecha, hora_status=id_hora)   
#       Calcula Almacenaje
                dalmacen = Segpaag.objects.get(compania='300', agencia='001', aplicacion='CAR', parametro='dias_gracia_alm').valor
                halmacen = Segpaag.objects.get(compania='300', agencia='001', aplicacion='CAR', parametro='hora_corte_alm').hora

                dias_tiempo = id_fecha - fecha_confirma
                dias_transcurridos = dias_tiempo.days
   
                if (hora_confirma >= halmacen):
                    dias_transcurridos = dias_transcurridos + 1
   
                dalmacen = int(dalmacen)
                dias_extra = dias_transcurridos - dalmacen

                if (dias_transcurridos > dalmacen):
                    id_tarifa = Cartitar.objects.get(tipo='A', status='A').tarifa
                    cartaralm = Cartaralm.objects.filter(tarifa=id_tarifa, fecha_inicio__lt=id_fecha, fecha_final__gte=id_fecha, status='A').values()
                    for taralm in cartaralm:
                        peso_base = taralm['peso_base']
                        valor_base = taralm['valor_base']
                        peso_adic = taralm['peso_adicional']
                        valor_peso_adic = taralm['valor_peso_adic']

                        if id_peso > peso_base:
                            valor = valor_base
                            peso_xtra = id_peso - peso_base
                            factor_peso_adic = peso_xtra / peso_adic
                            valor = valor + factor_peso_adic * valor_peso_adic
                        else:
                            valor = valor_base
                
                        valor = valor * dias_extra
                        Cardeent.objects.create(fecha=id_fecha, fecha_manifiesto=m_fecha, operador=id_operador,
                                        numero_vuelo=id_numero_vuelo, no_embarque=id_no_embarque, tarifa=id_tarifa,
                                        monto= valor, status='A', fecha_status=id_fecha, hora_status=id_hora)

            return JsonResponse('Calculado', safe=False)
        except Cargcaman.DoesNotExist:
            return JsonResponse({'Error': 'No hay para calcular'}, status=404)

def mostrar_calculos(request):
    id_fecha = request.GET.get('fecha')
    id_operador = request.GET.get('operador')
    id_numero_vuelo = request.GET.get('numero_vuelo')
    id_no_embarque = request.GET.get('no_embarque')
    cardeent = Cardeent.objects.filter(fecha=id_fecha, operador=id_operador, id_numero_vuelo=id_numero_vuelo,
                                       no_embarque=id_no_embarque).values()
    
    try:
        for card in cardeent:
            id_tarifa = card['tarifa']
            nom_tarifa = Cargcaman.objects.get(cargo=id_tarifa).nombre
            card['nom_tarifa'] = nom_tarifa

            if card['status'] == "A":
                card['nom_status'] = "Activo"
            else:
                card['nom_status'] = "Inactivo"
        
        cardeent_list = list(cardeent)
        return JsonResponse(cardeent_list, safe=False)

    except Cardeent.DoesNotExist:
        return JsonResponse({'Error':'No hay informacion'}, status=404)
    

def control_despacho(request):
    carentre = Carentre.objects.all().values()
    try:
        for car in carentre:
            id_operador = car['operador']
            nom_operador = Caropera.objects.get(operador=id_operador).nombre
            car['nom_operador'] = nom_operador
            if car['status'] == "G":
                car['nom_status'] = "Generado"
            else:
                car['nom_status'] = "Despachado" 
                
        carentre_list = list(carentre)
        return JsonResponse(carentre_list, safe=False)
    except Carentre.DoesNotExist:
        return JsonResponse({'Error', 'No hay información'}, status=404)
    
def detalle_despacho(request):
        id_fecha = request.GET.get('id_fecha')
        id_fecha_manifiesto = request.GET.get('id_fecha_manifiesto')
        id_operador = request.GET.get('id_operador')
        id_numero_vuelo = request.GET.get('id_numero_vuelo')
        id_no_embarque = request.GET.get('id_no_embarque')
    
    
        cardeent = Cardeent.objects.filter(fecha=id_fecha, fecha_manifiesto=id_fecha_manifiesto, 
                                       operador=id_operador, numero_vuelo=id_numero_vuelo,
                                       no_embarque=id_no_embarque).values()
        try:
            for car in cardeent:
                id_cargo = car['tarifa']
                nom_cargo = Cargcaman.objects.get(cargo=id_cargo).nombre
                car['nom_tarifa'] = nom_cargo

                if car['status'] == "A":
                    car['nom_status'] = "Activo"
                else:
                    car['nom_staus'] = "Inactivo"
        
            cardeent_list = list(cardeent)
            return JsonResponse(cardeent_list, safe=False)

        except Cardeent.DoesNotExist:
            return JsonResponse({'error:', 'No hay informacion'}, status=404)
    
def clientes_default(request):
    id_cliente = request.GET.get('cliente')
    crmclte = Crmclte.objects.filter(cliente=id_cliente).values()
    try:
        for clte in crmclte:
            if clte['code_id'] == 'N':
                clte['nom_code_id'] = 'Natural'
            else:
                clte['nom_code_id'] = 'Jurídico'

            if clte['status'] == 'A':
                clte['nom_status'] = 'Activo'
            if clte['status'] == 'I':
                clte['nom_status'] = 'Inactivo'

        crmclte_list = list(crmclte)
        return JsonResponse(crmclte_list, safe=False)

    except Crmclte.DoesNotExist:
        return JsonResponse({'Error': 'No hay información'}, status=404)
    
def define_almacenes(request):
    logalma = Logalma.objects.all().values()
    try:
        for alma in logalma:
            if alma['tipo_almacen'] == "P":
                alma['nom_tipo_almacen'] = 'Normal'

            if alma['tipo_almacen'] == "C":
                alma['nom_tipo_almacen'] = "Cuarto Frío"

            if alma['status'] == "A":
                alma['nom_status'] = "Activo"
            else:
                alma['nom_status'] = "Inactivo"
        
        logalma_list = list(logalma)
        return JsonResponse(logalma_list, safe=False)
    except Logalma.DoesNotExist:
        return JsonResponse({'Error' :' No hay información'}, status=404)

def control_movimientos(request):
        logctmo = Logctmo.objects.all().values()
        try:
            for ctmo in logctmo:
                id_cliente = ctmo['cliente']
                ctmo['nom_cliente']= Crmclte.objects.get(cliente=id_cliente).nombre_comercial
                id_codigo = ctmo['codigo']
                ctmo['nom_codigo'] = Logtral.objects.get(codigo=id_codigo).descripcion
                if ctmo['status'] == "I":
                    ctmo['nom_status'] = "Ingresada"
                if ctmo['status'] == "C":
                    ctmo['nom_status'] = "Calculada"
                if ctmo['status'] == "D":
                    ctmo['nom_status'] = "Despachada"
        
            logctmo_list = list(logctmo)
            return JsonResponse(logctmo_list, safe=False)
        except Logctmo.DoesNotExist:
            return JsonResponse({'Error' : 'No hay información que mostrar'}, status=404)
    
def detalles_movimientos(request):
        id_compania = request.GET.get('id_compania')
        id_agencia = request.GET.get('id_agencia')
        id_fecha = request.GET.get('id_fecha')
        id_almacen = request.GET.get('id_almacen')
        id_codigo = request.GET.get('id_codigo')
        id_documento = request.GET.get('id_documento')
     
        logdemo = Logdemo.objects.filter(compania=id_compania, agencia=id_agencia, fecha=id_fecha, almacen=id_almacen, codigo=id_codigo, documento=id_documento).values()
        try:
            for demo in logdemo:
                if demo['status'] == "I":
                    demo['nom_status'] = "Ingresada"
                if demo['status'] == "C":
                    demo['nom_status'] = "Calculada"
                if demo['status'] == "D":
                    demo['nom_status'] = "Despachada"
        
            logdemo_list = list(logdemo)
            return JsonResponse(logdemo_list, safe=False)
        except Logdemo.DoesNotExist:
            return JsonResponse({'Error': 'No hay información'}, status=404)

def calculo_cuartofrio(request):
        id_reg = request.GET.get('id')
        logctmo = Logctmo.objects.filter(id=id_reg).values()
        now = datetime.now()
        id_fecha = now.date()
        w_hora = now.time()
        id_hora = w_hora.strftime('%H:%M:%S')
        try:
            for ctmo in logctmo:
                id_compania = ctmo['compania']
                id_agencia = ctmo['agencia']
                idw_fecha = ctmo['fecha']
                id_almacen = ctmo['almacen']
                id_codigo = ctmo['codigo']
                id_documento = ctmo['documento']
                id_fecha_llegada = ctmo['fecha_llegada']
                id_hora_llegada = ctmo['hora_llegada']
            
                dias = id_fecha - id_fecha_llegada
                dias_servicio = dias.days
                cartari = Cartari.objects.filter(tarifa='03', fecha_inicio__lt=id_fecha, fecha_final__gte=id_fecha,
                                            status='A').values()
                for tari in cartari:
                    id_entrada = tari['entrada']
                    id_costo_diario = tari['costo_diario']
                    id_minimo_diario = tari['minimo_diario']
                    id_full_pallet = tari['full_pallet']
                    id_peso_base = tari['peso_base']

                logdemo = Logdemo.objects.filter(compania=id_compania, agencia=id_agencia, fecha=idw_fecha,
                            almacen=id_almacen, codigo=id_codigo, documento=id_documento).values()
            
                for demo in logdemo:
                    id_demo = demo['id']
                    id_secuencia = demo['secuencia']
                    id_pallets = demo['pallets']
                    id_peso = demo['peso']
                    id_cajas = demo['cajas']
                    entrada = id_entrada
                    if id_pallets > 0:
                        valor = id_pallets * id_full_pallet
                    if id_cajas > 0:
                        if id_peso > id_peso_base: 
                            peso_dif = id_peso - id_peso_base
                            valor = valor + peso_dif * id_costo_diario
                        else:
                            valor = 0 
                        if valor < id_minimo_diario:
                            valor = id_minimo_diario

                    valorf = valor * dias_servicio
                    valorf = valorf + entrada
                

                    Logdemo.objects.filter(id=id_demo).update(monto=valorf, status='C', modificado_por='contesis',
                            fecha_status=id_fecha, hora_status=id_hora)

                resultado = Logdemo.objects.filter(compania=id_compania, agencia=id_agencia, fecha=idw_fecha,
                        almacen=id_almacen, codigo=id_codigo, documento=id_documento).aggregate(
                        total=Sum('monto'))
            
                total_ctmo = decimal.Decimal(resultado['total'])
            
                Logctmo.objects.filter(id=id_reg).update(valor=total_ctmo, status='C', modificado_por='contesis',
                        fecha_status=id_fecha, hora_status=id_hora)
                Logctmo.save()
                Logdemo.save()
            return JsonResponse('Se generó el calculo...', safe=False)    
        except Logctmo.DoesNotExist:
            return JsonResponse({'Error ':'No hay información por mostrar'}, status=404)

def despacho_cuartofrio(request):
    id_registro = request.GET.get('id')
    now = datetime.now()
    id_fecha = now.date()
    w_hora = now.time()
    id_hora = w_hora.strftime('%H:%M:%S')
    logtral = Logtral.objects.filter(accion='R', maneja_cliente='S').values()
    for tral in logtral:
        id_codigo = tral['codigo']
        id_secuencia = tral['secuencia']
        if id_secuencia != 'number':
            id_secuencia = 0

        id_documento = id_secuencia + 1
    
    logctmo = Logctmo.objects.filter(id=id_registro).values()
    try:
        for ctmo in logctmo:
            id_compania = ctmo['compania']
            id_agencia = ctmo['agencia']
            ant_fecha = ctmo['fecha']
            ant_codigo = ctmo['codigo']
            id_almacen = ctmo['almacen']
            ant_documento = ctmo['documento']
            id_guia = ctmo['guia_despacho']

            id_cliente = ctmo['cliente']
            id_valor = ctmo['valor']

        Logctmo.objects.create(compania=id_compania, agencia=id_agencia, fecha=id_fecha, almacen=id_almacen,
                    codigo=id_codigo, documento=id_documento, fecha_creado=id_fecha, hora_creado=id_hora,
                    guia_despacho=id_guia, cliente=id_cliente, valor=id_valor, status='D')
    
        logdemo = Logdemo.objects.filter(compania=id_compania, agencia=id_agencia, fecha=ant_fecha, 
                    almacen=id_almacen, codigo=ant_codigo, documento=ant_documento).values()
    
        for demo in logdemo:
            id_orden = demo['orden_produccion']
            id_sec = demo['secuencia']
            id_pallets = demo['pallets']
            id_cajas = demo['cajas']
            id_peso = demo['peso']
            id_monto = demo['monto']
            Logdemo.objects.create(compania=id_compania, agencia=id_agencia, fecha=id_fecha, almacen=id_almacen,
                        codigo=id_codigo, documento=id_documento, secuencia=id_sec, orden_produccion=id_orden,
                        pallet_desp=id_pallets, peso_desp=id_peso, cajas_desp=id_cajas, monto=id_monto, status='D')

        Logctmo.objects.filter(id=id_registro).update(status='D', modificado_por='contesis', 
                                    fecha_status=id_fecha, hora_status=id_hora)
    
        Logdemo.objects.filter(compania=id_compania, agencia=id_agencia, fecha=ant_fecha, almacen=id_almacen,
                           codigo=ant_codigo, documento=ant_documento).update(status='D', modificado_por='contesis',
                            fecha_status=id_fecha, hora_status=id_hora)
    
        Logtral.objects.filter(codigo=id_codigo).update(secuencia=id_documento)

        return JsonResponse('Se generó el despacho satisfactoriamente...', safe=False)
    except Logctmo.DoesNotExist:
        return JsonResponse({'Error': ' No se encontró la entrada...'}, status=404)


#nuevo filtrado en tabla        
class CardmaniFilterView(generics.ListAPIView):
    queryset = Cardmani.objects.all()
    serializer_class = CardmaniSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['numero_vuelo']  # Aquí defines los campos por los que quieres filtrar

class CaratvuedFilterView(generics.ListAPIView):
    queryset = Caratvued.objects.all()
    serializer_class = CaratvuedSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['fecha', 'compania', 'matricula']

class CompaniaFilterView(generics.ListAPIView):
    queryset = Carcoaer.objects.all()
    serializer_class = CarcoaerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status']

class CaratenvueFilterView(generics.ListAPIView):
    queryset = Caratenvue.objects.all()
    serializer_class = CaratenvueSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status']

class PuertosFilterView(generics.ListAPIView):
    queryset = Puertos.objects.all()
    serializer_class = PuertosSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status'] 

class NaturalezaFilterView(generics.ListAPIView):
    queryset = Carnatur.objects.all()
    serializer_class = CarnaturSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status']

class LogtralFilterView(generics.ListAPIView):
    queryset = Logtral.objects.all()
    serializer_class = LogtralSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_field = ['status']

class CrmclteFilterView(generics.ListAPIView):
    queryset = Crmclte.objects.all()
    serializer_class = CrmclteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_field = ['status']