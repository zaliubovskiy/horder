from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Product


class ProductView(ListView):
    """list of models"""
    model = Product
    queryset = Product.objects.all()
    template_name = "product_detail.html"


class ProductDetailView(DetailView):
    """full description of the 3d Model"""
    model = Product
    slug_field = "url"
