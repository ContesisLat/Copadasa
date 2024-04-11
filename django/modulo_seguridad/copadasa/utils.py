from datetime import datetime

def convertir_fecha_personalizada(fecha):
    # Suponiendo que la fecha tiene el formato 'dd/mm/YYYY'
    formato_entrada = "%d/%m/%Y"
    formato_salida = "%Y-%m-%d"  # El formato deseado para la salida

    # Intentar convertir la fecha al formato deseado
    try:
        fecha_convertida = datetime.strptime(fecha, formato_entrada).strftime(formato_salida)
    except ValueError:
        # Manejar el error si la fecha no tiene el formato esperado
        fecha_convertida = None

    return fecha_convertida
