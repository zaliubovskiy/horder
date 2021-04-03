from django.shortcuts import render
from django.views.generic.base import View

from .models import Product


class ProductView(View):
    """list of models"""
    def get(self, request):
        products = Product.objects.all()
        return render(request, "search.html")

