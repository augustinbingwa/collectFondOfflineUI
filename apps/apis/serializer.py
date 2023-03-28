from rest_framework import serializers
from .models import Client
from .models import Cotisation

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class CotisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cotisation
        fields = '__all__'

