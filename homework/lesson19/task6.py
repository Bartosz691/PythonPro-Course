#from django.db import models

# Create your models here.
#class Post(models.Model):
#  tytul = models.CharField(max_length=100)
#  opis = models.TextField()
#  cena = models.DecimalField(max_digits=8, decimal_places=2)
#  data_dodania = models.DateTimeField(auto_now_add=True)
  
#  def __str__(self):
#       return self.title
   
# Krok 3: Rejestracja modelu w pliku blog/admin.py
# Dzięki temu model 'Post' pojawi się w panelu administratora.
# from django.contrib import admin
# from .models import Post # Importujemy nasz model
# admin.site.register(Post) # Rejestrujemy model