from django.shortcuts import render
from .models import Product


def home(request):
    products = Product.objects.all()

    return render(request, "polls/home.html", {"products": products})