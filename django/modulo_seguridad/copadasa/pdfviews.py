import json
from .models import *
from .serializer import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def safe_str(value):
    """Convierte cualquier valor a string seguro para ReportLab"""
    if value is None:
        return ""
    return str(value)

def draw_safe(p, x, y, value):
    """Wrapper de drawString para evitar errores con int/None"""
    p.drawString(x, y, safe_str(value))

@csrf_exempt
def informe_entrega(request):
    if request.method == "POST":
        data = json.loads(request.body)

        # Respuesta PDF
        response = HttpResponse(content_type="application/pdf")
        response["Content-Disposition"] = 'attachment; filename="informe_entrega.pdf"'

        # Canvas PDF
        p = canvas.Canvas(response, pagesize=letter)
        width, height = letter

        # Dibujar borde alrededor de la página
        p.setLineWidth(2)
        p.rect(30, 30, width-60, height-60)
        p.setLineWidth(1) 

        p.setFont("Helvetica-Bold", 16)
        p.drawCentredString(width/2, 745, "COPADASA")

        p.setFont("Helvetica-Bold", 12)
        p.drawCentredString(width/2, 730, "INFORME DE ENTREGA")

        p.setFont("Helvetica", 11)

        # ================== CABECERA ==================
        draw_safe(p, 50, 700, "No. de vuelo:")
        p.line(115, 698, 250, 698)
        draw_safe(p, 120, 700, data.get("numero_vuelo"))

        draw_safe(p, 300, 700, "Fecha:")
        p.line(335, 698, 400, 698)
        draw_safe(p, 340, 700, data.get("fecha_manifiesto"))

        draw_safe(p, 50, 680, "Piezas declaradas:")
        p.line(145, 678, 185, 678)
        draw_safe(p, 148, 680, data.get("pieza_entrega"))

        draw_safe(p, 300, 680, "Peso declarado:")
        p.line(380, 678, 420, 678)
        draw_safe(p, 383, 680, data.get("peso"))

        draw_safe(p, 50, 660, "No. AWB:")
        p.line(100, 658, 250, 658)
        draw_safe(p, 105, 660, data.get("no_embarque"))

        draw_safe(p, 300, 660, "Contenido declarado:")
        p.line(405, 658, 530, 658)
        draw_safe(p, 410, 660, data.get("naturaleza"))

        draw_safe(p, 50, 640, "Consignatario:")
        p.line(120, 638, 250, 638)
        draw_safe(p, 125, 640, data.get("destinatario"))

        p.line(40, 620, 550, 620)
        p.line(40, 618, 550, 618)

        # ================== DATOS DE CARGA ==================
        draw_safe(p, 50, 590, "Carga entregada a:")
        p.line(145, 588, 250, 588)

        draw_safe(p, 300, 590, "Liquidacion aduana:")
        p.line(405, 588, 530, 588)
        draw_safe(p, 410, 590, data.get("liquida_aduana"))

        draw_safe(p, 50, 570, "Manifiesto:")
        p.line(105, 568, 250, 568)
        draw_safe(p, 110, 570, data.get("no_embarque"))

        draw_safe(p, 300, 570, "Fecha de entrega:")
        p.line(395, 568, 465, 568)
        draw_safe(p, 400, 570, data.get("fecha_entrega"))

        draw_safe(p, 50, 550, "Recibo de pago:")
        p.line(130, 548, 250, 548)

        draw_safe(p, 300, 550, "Hora:")
        p.line(330, 548, 370, 548)

        # ================== ESTADOS ==================
        p.setFont("Helvetica-Bold", 10)
        p.drawCentredString(width/2, 520, "ESTADO DE LA CARGA AL MOMENTO DE SU ENTREGA")
        p.line(170, 518, 445, 518)
        p.setFont("Helvetica", 11)

        draw_safe(p, 50, 490, "Piezas entregadas:")
        p.line(145, 488, 185, 488)
        draw_safe(p, 148, 490, data.get("pieza_entrega"))

        draw_safe(p, 300, 490, "Repesaje al entregar:")
        p.line(410, 488, 450, 488)

        draw_safe(p, 50, 470, "Piezas buenas:")
        p.line(125, 468, 165, 468)

        draw_safe(p, 300, 470, "Piezas faltantes:")
        p.line(380, 468, 420, 468)

        draw_safe(p, 50, 450, "Rotas:")
        p.line(85, 448, 125, 448)

        draw_safe(p, 300, 450, "Mojadas:")
        p.line(345, 448, 385, 448)

        draw_safe(p, 50, 430, "Golpeadas:")
        p.line(110, 428, 150, 428)

        draw_safe(p, 300, 430, "Reparadas:")
        p.line(360, 428, 400, 428)

        draw_safe(p, 70, 400, "Observaciones:")
        p.line(150, 398, 530, 398)
        p.line(150, 378, 530, 378)
        p.line(150, 358, 530, 358)
        p.line(150, 338, 530, 338)

        # ================== FIRMAS ==================
        p.setFont("Helvetica-Bold", 8)
        p.drawCentredString(width/2, 308, "REPRESENTANTE DEL CONSIGNATARIO QUE RECIBE LA CARGA DE ACUERDO CON ESTE INFORME")
        p.line(109, 306, 503, 306)
        p.setFont("Helvetica", 11)

        draw_safe(p, 60, 250, "Nombre en letra imprenta")
        p.line(40, 260, 200, 260)

        draw_safe(p, 280, 250, "Cédula")
        p.line(250, 260, 350, 260)

        draw_safe(p, 460, 250, "Firma")
        p.line(400, 260, 550, 260)

        draw_safe(p, 60, 210, "Recibo por almacenaje")
        p.line(40, 220, 200, 220)

        draw_safe(p, 285, 210, "Placa")
        p.line(250, 220, 350, 220)

        draw_safe(p, 425, 210, "Carga verificada por")
        p.line(400, 220, 550, 220)

        draw_safe(p, 70, 170, "Informe hecho por")
        p.line(40, 180, 200, 180)
        draw_safe(p, 45, 182, data.get("hecho_por"))

        # Guardar PDF
        p.showPage()
        p.save()
        return response