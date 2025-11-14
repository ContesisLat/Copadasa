from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import connections
from .serializer import *
from django.http import JsonResponse
from django.db import transaction
from datetime import datetime, date, timedelta


class InsertView(APIView):
    """
    Vista para manejar la inserción de registros en cualquier tabla especificada.
    """
    @transaction.atomic
    def post(self, request):
        """
        Maneja las solicitudes POST para insertar un nuevo registro en la base de datos.
        """
        table_name = request.data.get('model')
        fields = request.data.get('data')
                
        if not table_name or not fields:
            return Response({"error": "Faltan datos o nombre de la tabla"}, status=status.HTTP_400_BAD_REQUEST)

        print(table_name)
        try:
            with transaction.atomic():    
                print('en transaccion')    
                if table_name == 'logctmo':   
                    id_codigo = fields['codigo']
                    id_usuario = fields['creado_por']
            
                    try:  
                        #id_secuencia = Logtral.objects.select_for_update().raw("select c.sec_reserva from logtral c where c.codigo = '", id_codigo, '"')
                        #logtral = Logtral.objects.filter(codigo=id_codigo).values()
                        if Logtral.objects.filter(codigo=id_codigo).exists():
                            sec_reserva = Logtral.objects.get(codigo=id_codigo).sec_reserva 
                            if sec_reserva is None:
                                idw_secuencia = 0
                            else:
                                idw_secuencia = int(sec_reserva)

                            id_secuencia = idw_secuencia + 1
                            Logtral.objects.filter(codigo=id_codigo).update(sec_reserva=id_secuencia)
                            sec_reserva = id_secuencia
                            fields['documento'] = str(id_secuencia)

                            Carussec.objects.filter(usuario=id_usuario, tabla=table_name).delete()
                            Carussec.objects.create(usuario=id_usuario, tabla=table_name, secuencia=id_secuencia)
                    except Exception as e:
                        print('error')   
                        return Response({"error": f"Error durante el acceso al secuencial: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

                if table_name == 'cartaralm':
                    try: 
                        id_fecha_inicio = fields['fecha_inicio']
                        id_tarifa = fields['tarifa'] 
                        cartaralm_filtrado = Cartaralm.objects.filter(tarifa=id_tarifa)
                        cartaralm = cartaralm_filtrado.latest('fecha_inicio')
                        fecha = cartaralm.fecha_inicio
                        formato = "%Y-%m-%d"
                        fechainicio = datetime.strptime(id_fecha_inicio, formato)
                        fechainicio = fechainicio - timedelta(days=1)
                        Cartaralm.objects.filter(tarifa=id_tarifa, fecha_inicio=fecha).update(fecha_final=fechainicio)
                    except Exception as e:
                        print('error')   
                        return Response({"error": f"Error cerrando la vigencia anterior: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

                if table_name == 'cartari': 
                    try: 
                        print(table_name)
                        id_fecha_inicio = fields['fecha_inicio']
                        id_tarifa = fields['tarifa'] 
                        cartari_filtrado = Cartari.objects.filter(tarifa=id_tarifa)
                        cartari = cartari_filtrado.latest('fecha_inicio')
                        fecha = cartari.fecha_inicio
                        formato = "%Y-%m-%d"
                        fechainicio = datetime.strptime(id_fecha_inicio, formato)
                        fechainicio = fechainicio - timedelta(days=1)
                        Cartari.objects.filter(tarifa=id_tarifa, fecha_inicio=fecha).update(fecha_final=fechainicio)
                        print('Cerro vigencia')
                    except Exception as e:
                        print('error')   
                        return Response({"error": f"Error cerrando la vigencia anterior: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
            
                # Construye la consulta SQL de inserción
                columns = ', '.join(fields.keys())
                placeholders = ', '.join(['%s'] * len(fields))
                sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

                try:
                    with connections['copadasa_db'].cursor() as cursor:
                        cursor.execute(sql, list(fields.values()))
                        return JsonResponse({"success": True}, status=201)
                except Exception as e:
                    print(f"Error during INSERT operation: {str(e)}")
                return JsonResponse({"error": str(e)}, status=400)
        except Exception as e:
            print(f"Error during INSERT operation: {str(e)}")
            return JsonResponse({"error": str(e)}, status=400)
        
class UpdateView(APIView):
    """
    Vista para manejar la actualización de registros en cualquier modelo especificado.
    """
    def post(self, request):
        # Obtiene el nombre de la tabla desde la solicitud
        table_name = request.data.get('table')
        filters = request.data.get('filters')
        updated_data = request.data.get('data')

        if not table_name or not filters or not updated_data:
           
            return Response({"error": "Faltan datos para la operación"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Construir la consulta SQL para la actualización
            set_clause = ', '.join([f"{key} = %s" for key in updated_data.keys()])
            where_clause = ' AND '.join([f"{key} = %s" for key in filters.keys()])

            query = f"UPDATE {table_name} SET {set_clause} WHERE {where_clause}"
            params = list(updated_data.values()) + list(filters.values())

            print(query)
            
            # Ejecutar la consulta
            with connections['copadasa_db'].cursor() as cursor:
                cursor.execute(query, params)

            return Response({"message": "Registro actualizado exitosamente"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": f"Error durante la operación de actualización: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)


class DeleteView(APIView):
    """
    Vista para manejar la eliminación de registros en cualquier tabla especificada.
    """

    def post(self, request):
        # Obtener datos de la solicitud
        table_name = request.data.get('table')
        filters = request.data.get('filters')  # Diccionario con las condiciones para la eliminación

        if not table_name or not filters:
            return Response({"error": "Faltan datos para la operación"}, status=status.HTTP_400_BAD_REQUEST)

        # Construir la consulta SQL
        where_clause = ' AND '.join([f"{key} = %s" for key in filters.keys()])
        sql_query = f"DELETE FROM {table_name} WHERE {where_clause}"

        params = list(filters.values())

        # Ejecutar la consulta en la base de datos Informix
        try:
            with connections['copadasa_db'].cursor() as cursor:
                cursor.execute(sql_query, params)
            return Response({"status": "Success"}, status=status.HTTP_200_OK)
        except Exception as e:
            print(f"Error during DELETE operation: {e}")
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

