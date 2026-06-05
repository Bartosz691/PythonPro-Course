from django.contrib import admin
from .models import Ogłoszenie

@admin.register(Ogłoszenie)
class OgloszenieAdmin(admin.ModelAdmin):
    list_display = ('tytul', 'cena', 'data_dodania')