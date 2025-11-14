from django.contrib import admin
from django.urls import path
from .pdfviews import *
from .excelviews import *
from rest_framework import routers
from .viewsets import *
from .views import *
from .crud import *

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
route.register('logarea', LogareaViewSet)
route.register('logalma', LogalmaViewSet)
route.register('paises',PaisesViewSet)
route.register('puertos',PuertosViewSet)
route.register('ubicacion',UbicacionViewSet)
route.register('logtral', LogtralViewSet)
route.register('logctmo', LogctmoViewSet)
route.register('logdemo', LogdemoViewSet)
route.register('crmclte', CrmclteViewSet)

urlpatterns = [
    path('paises/ciudad', ciudades_por_pais, name='ciudades_por_pais'),
    path('paises/puertos', puertos_por_pais, name='puertos_por_pais'),
    path('logarea/loganaquel', anaqueles_por_area, name='anaqueles_por_area'),
    path('loganaquel/logubica', anaqueles_por_ubicacion, name='anaqueles_por_ubicacion'),
    path('caratenvue/', cargos_aereos, name="cargos_aereos"),
    path('cartiaero/cartarvue', tarifas_aeronaves, name='tarifas_aeronaves'),
    path('carnatur/', naturaleza_cargos, name='naturaleza_cargos'),
    path('cargcaman/', cargos_manejo, name='cargos_manejo'),
    path('cargcaman/cartarman', tarifas_manejo, name='tarifas_manejo'),
    path('cartaralm/', tarifas_almacenaje, name='tarifas_almacenaje'),
    path('carinent/', indicadores_carga, name='indicadores_carga'),
    path('cartari/', tarifas_frio, name='tarifas_frio'),
    path('carcmani/', control_manifiesto, name='control_manifiesto'),
    path('logtral/', transacciones_almacen, name='transacciones_almacen' ),
    path('logctmo/', control_movimientos, name='control_movimientos'),
    path('logctmo/logdemo', detalles_movimientos, name='detalles_movimientos'),
    path('cardeent/mostrar', mostrar_calculos, name='mostrar_calculos'),
    path('carcmani/cardmani', detalle_manifiesto, name='detalle_manifiesto'),
    path('carentre/', control_despacho, name='control_despacho'),
    path('carentre/cardeent', detalle_despacho, name='detalle_despacho'),
    path('carcmani/calculo', calcula_manifiesto, name='calcula_manifiesto'),
    path('logctmo/calculo', calculo_cuartofrio, name='calculo_cuartofrio'),
    path('logctmo/salida', despacho_cuartofrio, name="despacho_ctofrio"),
    path('crmclte/', clientes_default, name='clientes_default'),
    path('logalma/', define_almacenes, name='define_almacenes'),
    path('cartarvue/tarifas', tarifas_servaereo, name="tarifa_servaereo"),
    path('cardmani/filter', CardmaniFilterView.as_view(), name='cardmani-filter'),
    path('caratvued/filter', CaratvuedFilterView.as_view(), name='servuelos-filter'),
    path('puertos/filter', PuertosFilterView.as_view(), name='puertos-filter'),
    path('compania/filter', CompaniaFilterView.as_view(), name='compania-filter'),
    path('naturaleza/filter', NaturalezaFilterView.as_view(), name='naturaleza-filter'),
    path('caratenvue/filter', CaratenvueFilterView.as_view(), name='caratenvue-filter'),
    path('logtral/filter', LogtralFilterView.as_view(), name='logtral-filter'),
    path('crmclte/filter', CrmclteFilterView.as_view(), name='crmclte-filter'),
    path('query',query_global, name='query_global'),
    path('guardar-imagenes',guardar_archivos, name='guardar-imagenes'),
    path('informe-entrega',informe_entrega, name='informe-entrega'),
    path('Regmani_excel',excel_regmani,name='Regmani_excel'),
    path('Caratvue_excel', excel_caratvue, name='Caratvue_excel'),
    path('Logctmo_excel', excel_logctmo, name="excel_logctmo"),
    path('AuxLogctmo_excel', excel_auxlogctmo, name="excel_auxlogctmo"),
    path('Caratvue_excel_resumen', excel_caratvue_resumen, name="excel_caratvue_resumen"),
    path('insert/', InsertView.as_view(), name='insert'),  # Ruta para insertar un nuevo registro
    path('update/', UpdateView.as_view(), name='update'),  # Ruta para actualizar un registro
    path('delete/', DeleteView.as_view(), name='delete'),  # Ruta para eliminar un registro
]
urlpatterns += route.urls