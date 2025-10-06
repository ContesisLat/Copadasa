from rest_framework import viewsets
from rest_framework.response import Response
from .models import *
from .serializer import *


class CaratenvueViewSet(viewsets.ModelViewSet):
    queryset = Caratenvue.objects.all()
    serializer_class = CaratenvueSerializer

class CaratvueViewSet(viewsets.ModelViewSet):
    queryset = Caratvue.objects.all()
    serializer_class = CaratvueSerializer

class CarcmaniViewSet(viewsets.ModelViewSet):
    queryset = Carcmani.objects.all()
    serializer_class = CarcmaniSerializer

class CarcoaerViewSet(viewsets.ModelViewSet):
    queryset = Carcoaer.objects.all()
    serializer_class = CarcoaerSerializer

class CardeentViewSet(viewsets.ModelViewSet):
    queryset = Cardeent.objects.all()
    serializer_class = CardeentSerializer

class CardmaniViewSet(viewsets.ModelViewSet):
    queryset = Cardmani.objects.all()
    serializer_class = CardmaniSerializer

class CarentreViewSet(viewsets.ModelViewSet):
    queryset = Carentre.objects.all()
    serializer_class = CarentreSerializer

class CargcamanViewSet(viewsets.ModelViewSet):
    queryset = Cargcaman.objects.all()
    serializer_class = CargcamanSerializer

class CarinentViewSet(viewsets.ModelViewSet):
    queryset = Carinent.objects.all()
    serializer_class = CarinentSerializer

class CarnaturViewSet(viewsets.ModelViewSet):
    queryset = Carnatur.objects.all()
    serializer_class = CarnaturSerializer

class CaroperaViewSet(viewsets.ModelViewSet):
    queryset = Caropera.objects.all()
    serializer_class = CaroperaSerializer

class CartaralmViewSet(viewsets.ModelViewSet):
    queryset = Cartaralm.objects.all()
    serializer_class = CartaralmSerializer

class CartariViewSet(viewsets.ModelViewSet):
    queryset = Cartari.objects.all()
    serializer_class = CartariSerializer

class CartarmanViewSet(viewsets.ModelViewSet):
    queryset = Cartarman.objects.all()
    serializer_class = CartarmanSerializer

class CartarvueViewSet(viewsets.ModelViewSet):
    queryset = Cartarvue.objects.all()
    serializer_class = CartarvueSerializer

class CartiaeroViewSet(viewsets.ModelViewSet):
    queryset = Cartiaero.objects.all()
    serializer_class = CartiaeroSerializer

class CartitarViewSet(viewsets.ModelViewSet):
    queryset = Cartitar.objects.all()
    serializer_class = CartitarSerializer

class CarudlsViewSet(viewsets.ModelViewSet):
    queryset = Carudls.objects.all()
    serializer_class = CarudlsSerializer

class CiudadesViewSet(viewsets.ModelViewSet):
    queryset = Ciudades.objects.all()
    serializer_class = CiudadesSerializer

class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer

class CrmcorrViewSet(viewsets.ModelViewSet):
    queryset = Crmcorr.objects.all()
    serializer_class = CrmcorrSerializer

class CrmprovViewSet(viewsets.ModelViewSet):
    queryset = Crmprov.objects.all()
    serializer_class = CrmprovSerializer

class CaratvuedViewSet(viewsets.ModelViewSet):
    queryset = Caratvued.objects.all()
    serializer_class = CaratvuedSerializer

class LogubicaViewSet(viewsets.ModelViewSet):
    queryset = Logubica.objects.all()
    serializer_class = LogubicaSerializer

class LogareaViewSet(viewsets.ModelViewSet):
    queryset = Logarea.objects.all()
    serializer_class = LogareaSerializer

class LogalmaViewSet(viewsets.ModelViewSet):
    queryset = Logalma.objects.all()
    serializer_class = LogalmaSerializer
    

class PaisesViewSet(viewsets.ModelViewSet):
    queryset = Paises.objects.all()
    serializer_class = PaisesSerializer

class PuertosViewSet(viewsets.ModelViewSet):
    queryset = Puertos.objects.all()
    serializer_class = PuertosSerializer

class UbicacionViewSet(viewsets.ModelViewSet):
    queryset = Ubicacion.objects.all()
    serializer_class = UbicacionSerializer

class LogtralViewSet(viewsets.ModelViewSet):
    queryset = Logtral.objects.all()
    serializer_class = LogtralSerializer

class LogctmoViewSet(viewsets.ModelViewSet):
    queryset = Logctmo.objects.all()
    serializer_class = LogctmoSerializer

class LogdemoViewSet(viewsets.ModelViewSet):
    queryset = Logdemo.objects.all()
    serializer_class = LogdemoSerializer

class SegpaagViewSet(viewsets.ModelViewSet):
    queryset = Segpaag.objects.all()
    serializer_class = SegpaagSerializer

class CrmclteViewSet(viewsets.ModelViewSet):
    queryset = Crmclte.objects.all()
    serializer_class = CrmclteSerializer