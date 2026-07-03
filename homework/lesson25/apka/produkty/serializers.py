from rest_framework import serializers
from .models import Produkt

class ProduktSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produkt # wskazujemy, który model ma być serializowany
        fields = '__all__'
        
