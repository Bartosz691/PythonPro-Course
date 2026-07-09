from rest_framework import serializers

from .models import Produkt, Note


class ProduktSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produkt
        fields = "__all__"


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"