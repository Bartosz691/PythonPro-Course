from django.contrib import admin

from .models import Category, Product, Note


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category")


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("id", "title")