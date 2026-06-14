from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import ProductForm
from .models import Product, Note


def info_view(request):
    return HttpResponse("Informacje o stronie")


def rules_view(request):
    return HttpResponse("Regulamin")


def user_view(request, username):
    return HttpResponse(f"Witaj na profilu, {username}!")


def product_list_view(request):
    products = Product.objects.all()
    return render(request, "strona/product_list.html", {"products": products})


def product_create_view(request):
    if request.method == "POST":
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("product-list")
    else:
        form = ProductForm()

    return render(request, "strona/product_form.html", {"form": form})


def category_products_view(request, category_id):
    products = Product.objects.filter(category_id=category_id)
    return render(request, "strona/product_list.html", {"products": products})


def note_list_view(request):
    notes = Note.objects.all().order_by("id")

    paginator = Paginator(notes, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "strona/note_list.html", {"page_obj": page_obj})


def note_detail_view(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    return render(request, "strona/note_detail.html", {"note": note})