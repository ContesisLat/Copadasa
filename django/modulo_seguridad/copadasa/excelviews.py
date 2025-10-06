from rest_framework.decorators import api_view
from rest_framework.response import Response
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment
from openpyxl.utils import get_column_letter
from django.http import HttpResponse
import json
import logging

# Configurar logging para depuración
logger = logging.getLogger(__name__)

@api_view(['POST'])
def excel_regmani(request):
    # Parsear el cuerpo de la solicitud
    try:
        vue_data = json.loads(request.body) if request.body else {}
        logger.info("Datos recibidos: %s", vue_data)  # Para depuración
    except json.JSONDecodeError:
        logger.error("Error al parsear JSON: %s", request.body)
        return Response({"error": "Invalid JSON data"}, status=400)

    # Validar que todos los campos de nivel raíz estén presentes
    required_fields = [
        "operador", "aeronave_matricula", "puerto_despacho",
        "puerto_destino", "fecha", "no_vuelo", "tabla"
    ]
    missing_fields = [field for field in required_fields if field not in vue_data or vue_data[field] is None]
    if missing_fields:
        logger.error("Campos obligatorios faltantes: %s", missing_fields)
        return Response({"error": f"Missing required fields: {', '.join(missing_fields)}"}, status=400)

    # Extraer los campos
    operador = vue_data["operador"]
    aeronave_matricula = vue_data["aeronave_matricula"]
    puerto_despacho = vue_data["puerto_despacho"]
    puerto_destino = vue_data["puerto_destino"]
    fecha = vue_data["fecha"]
    no_vuelo = vue_data["no_vuelo"]
    tabla = vue_data["tabla"]

    # Validar que tabla sea un arreglo
    if not isinstance(tabla, list):
        logger.error("El campo 'tabla' debe ser un arreglo")
        return Response({"error": "'tabla' must be an array"}, status=400)

    # Validar que cada elemento de tabla tenga los campos requeridos (excepto destino y peso)
    required_tabla_fields = ["guia", "items", "naturaleza", "destinatario"]
    for index, item in enumerate(tabla):
        missing_tabla_fields = [field for field in required_tabla_fields if field not in item or item[field] is None]
        if missing_tabla_fields:
            logger.error("Campos faltantes en el elemento %d de 'tabla': %s", index, missing_tabla_fields)
            return Response({"error": f"Missing fields in tabla item {index}: {', '.join(missing_tabla_fields)}"}, status=400)

    # Create a new workbook and select the active sheet
    wb = Workbook()
    ws = wb.active
    ws.title = "Manifiesto de Carga"

    # Set up fonts and alignment
    center_alignment = Alignment(horizontal="center")

    # Sección del encabezado
    ws.merge_cells('A1:G1')
    ws['A1'] = "CARGO MANIFEST"
    ws['A1'].font = Font(name="Arial", size=16, bold=True)
    ws['A1'].alignment = center_alignment

    ws.merge_cells('A2:G2')
    ws['A2'] = "MANIFIESTO DE CARGA"
    ws['A2'].font = Font(name="Arial", size=18, bold=False)
    ws['A2'].alignment = center_alignment

    ws['A4'] = "OWNER OR OPERATOR"
    ws['A4'].font = Font(name="Arial", size=8, bold=False)

    ws.merge_cells('C4:F4')
    ws['C4'] = operador
    ws['C4'].font = Font(name="Arial", size=14, bold=True)
    ws['C4'].alignment = center_alignment

    ws['A5'] = "Propietario o Administrador"
    ws['A5'].font = Font(name="Arial", size=8, bold=False)

    ws['A6'] = "AIRCRAFT"
    ws['A6'].font = Font(name="Arial", size=6, bold=True)

    ws['E6'] = "MARKS OF NATIONALITY AND REGISTRATION"
    ws['E6'].font = Font(name="Arial", size=6, bold=False)

    ws['G6'] = "FLIGHT NO."
    ws['G6'].font = Font(name="Arial", size=6, bold=False)

    ws['A7'] = "Aeronave"
    ws['A7'].font = Font(name="Arial", size=6, bold=False)

    ws['E8'] = "MARCAS DE NACIONALIDAD Y MATRICULA"
    ws['E8'].font = Font(name="Arial", size=6, bold=False)

    ws['G8'] = "VUELO NO."
    ws['G8'].font = Font(name="Arial", size=6, bold=False)

    ws['A9'] = operador.split()[0]
    ws['A9'].font = Font(name="Arial", size=20, bold=True)

    ws.merge_cells('E9:F9')
    ws['E9'] = aeronave_matricula
    ws['E9'].font = Font(name="Arial", size=20, bold=True)

    ws['G9'] = no_vuelo
    ws['G9'].font = Font(name="Arial", size=20, bold=True)

    ws['A10'] = "POINT OF LOADING"
    ws['A10'].font = Font(name="Arial", size=6, bold=False)

    ws['E10'] = "POINT OF UNLOADING"
    ws['E10'].font = Font(name="Arial", size=6, bold=False)

    ws['G10'] = "DATE"
    ws['G10'].font = Font(name="Arial", size=6, bold=False)

    ws['A11'] = "PUNTO DE EMBARQUE"
    ws['A11'].font = Font(name="Arial", size=6, bold=False)

    ws['E11'] = "PUNTO DE DESCARGA"
    ws['E11'].font = Font(name="Arial", size=6, bold=False)

    ws['G11'] = "FECHA"
    ws['G11'].font = Font(name="Arial", size=8, bold=False)

    ws.merge_cells('A12:B12')
    ws['A12'] = puerto_despacho
    ws['A12'].font = Font(name="Arial", size=20, bold=True)

    ws.merge_cells('E12:F12')
    ws['E12'] = puerto_destino
    ws['E12'].font = Font(name="Arial", size=20, bold=True)

    ws['G12'] = fecha
    ws['G12'].font = Font(name="Arial", size=20, bold=True)

    # Encabezado de la tabla
    ws['A13'] = "AIR WAYBILL"
    ws['A13'].font = Font(name="Arial", size=6, bold=False)
    ws['A13'].alignment = center_alignment

    ws['B13'] = "NUMBER"
    ws['B13'].font = Font(name="Arial", size=6, bold=False)
    ws['B13'].alignment = center_alignment

    ws['C13'] = "WEIGHT"
    ws['C13'].font = Font(name="Arial", size=6, bold=False)
    ws['C13'].alignment = center_alignment

    ws['D13'] = "DESTINO"
    ws['D13'].font = Font(name="Arial", size=6, bold=False)
    ws['D13'].alignment = center_alignment

    ws['E13'] = "NATURE OF GOODS"
    ws['E13'].font = Font(name="Arial", size=6, bold=False)
    ws['E13'].alignment = center_alignment

    ws['F13'] = "CONSIGNEE AND ADDRESS"
    ws['F13'].font = Font(name="Arial", size=6, bold=False)
    ws['F13'].alignment = center_alignment

    ws['A14'] = "NUMBER"
    ws['A14'].font = Font(name="Arial", size=6, bold=False)
    ws['A14'].alignment = center_alignment

    ws['B14'] = "OF PIECES"
    ws['B14'].font = Font(name="Arial", size=6, bold=False)
    ws['B14'].alignment = center_alignment

    ws['C14'] = "KGS"
    ws['C14'].font = Font(name="Arial", size=6, bold=False)
    ws['C14'].alignment = center_alignment

    # Tabla
    start_data_row = 17
    for i, item in enumerate(tabla, start=start_data_row):
        try:
            ws.cell(row=i, column=1, value=item["guia"])
            ws.cell(row=i, column=2, value=item["items"] if item["items"] is not None else 0)
            # Asignar valor por defecto a peso si es inválido
            peso = item.get("peso", "0")
            if not peso.strip() or not peso.replace(".", "").isdigit():
                peso = "0"
            ws.cell(row=i, column=3, value=float(peso))
            ws.cell(row=i, column=4, value=item.get("destino", "PTY"))
            ws.cell(row=i, column=5, value=item["naturaleza"])
            ws.cell(row=i, column=6, value=item["destinatario"])
        except (KeyError, ValueError) as e:
            logger.error("Error al procesar elemento %d de tabla: %s", i - start_data_row, str(e))
            return Response({"error": f"Invalid data in tabla item {i - start_data_row}: {str(e)}"}, status=400)

    # Adjust column widths
    column_widths = [20, 6.14, 8.71, 4.57, 35.86, 41.57, 21.14]
    for i, width in enumerate(column_widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = width

    # Create response
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="cargo_manifest.xlsx"'
    wb.save(response)
    return response
