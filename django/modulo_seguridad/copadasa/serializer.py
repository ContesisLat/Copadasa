from rest_framework import serializers  
from .models import *

class CaratenvueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caratenvue
        fields = '__all__'

class CaratvueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caratvue
        fields = '__all__'

class CarcmaniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carcmani
        fields = '__all__'

class CarcoaerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carcoaer
        fields = '__all__'

class CardeentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cardeent
        fields = '__all__'

class CardmaniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cardmani
        fields = '__all__'

class CarentreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carentre
        fields = '__all__'


class CargcamanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargcaman
        fields = '__all__'

class CarinentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carinent
        fields = '__all__'

class CarnaturSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carnatur
        fields = '__all__'

class CaroperaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caropera
        fields = '__all__'

class CartaralmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartaralm
        fields = '__all__'

class CartariSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartari
        fields = '__all__'

class CartarmanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartarman
        fields = '__all__'

class CartarvueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartarvue
        fields = '__all__'

class CartiaeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartiaero
        fields = '__all__'

class CartitarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartitar
        fields = '__all__'

class CarudlsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carudls
        fields = '__all__'

class CiudadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudades
        fields = '__all__'

class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = '__all__'

class CrmcorrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crmcorr
        fields = '__all__'


class CrmprovSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crmprov
        fields = '__all__'

class CaratvuedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caratvued
        fields = '__all__'


class LogubicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logubica
        fields = '__all__'

class LogareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logarea
        fields = '__all__'

class LogalmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logalma
        fields = '__all__'
        

class PaisesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paises
        fields = '__all__'

class PuertosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Puertos
        fields = '__all__'

class UbicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubicacion
        fields = '__all__'

class LogtralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logtral
        fields = '__all__'

class LogctmoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logctmo
        fields = '__all__'

class LogdemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logdemo
        fields = '__all__'

class SegpaagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Segpaag
        fields = '__all__'

class CrmclteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crmclte
        fields = '__all__'