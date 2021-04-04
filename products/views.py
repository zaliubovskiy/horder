from django.shortcuts import render
from django.views.generic.base import View

from .models import Product


class ProductView(View):
    """list of models"""
    def get(self, request):
        products = Product.objects.all()
        return render(request, "product_detail.html", {"product_list": products})


class ProductDetailView(View):
    """full description of the 3d Model"""
    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        return render(request, "product_detail.html", {"product": product})
