from django.contrib import admin
from django.urls import path
from rest_framework import routers
from .viewsets import *
from .views import *

route = routers.SimpleRouter()
route.register('caratenvue',CaratenvueViewSet)
route.register('caratvue',CaratvueViewSet)
route.register('carcmani',CarcmaniViewSet)
route.register('carcoaer',CarcoaerViewSet)
route.register('cardeent',CardeentViewSet)
route.register('cardmani',CardmaniViewSet)
route.register('carentre',CarentreViewSet)
route.register('cargcaman',CargcamanViewSet)
route.register('carinent',CarinentViewSet)
route.register('carnatur',CarnaturViewSet)
route.register('caropera',CaroperaViewSet)
route.register('cartaralm',CartaralmViewSet)
route.register('cartari',CartariViewSet)
route.register('cartarman',CartarmanViewSet)
route.register('cartarvue',CartarvueViewSet)
route.register('cartiaero',CartiaeroViewSet)
route.register('cartitar',CartitarViewSet)
route.register('carudls',CarudlsViewSet)
route.register('ciudades',CiudadesViewSet)
route.register('clientes',ClientesViewSet)
route.register('crmcorr',CrmcorrViewSet)
route.register('crmprov',CrmprovViewSet)
route.register('caratvued',CaratvuedViewSet)
route.register('logubica',LogubicaViewSet)
route.register('paises',PaisesViewSet)
route.register('puertos',PuertosViewSet)
route.register('ubicacion',UbicacionViewSet)

urlpatterns = [
    path('paises/ciudad', ciudades_por_pais, name='ciudades_por_pais'),
    path('paises/puertos', puertos_por_pais, name='puertos_por_pais'),
]
urlpatterns += route.urls