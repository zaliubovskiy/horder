from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Product, Category, SubCategory


# class SubCategoryFilter:
#
#     def get_category(self):
#         return Category.objects.all()
#
#     def get_subcategory(self):
#         return SubCategory.objects.all()

class IndexView(ListView):
    """home page"""
    model = Product
    template_name = "index.html"


class ProductView(ListView):
    """list of models"""
    model = Product
    queryset = Product.objects.all()
    template_name = "search.html"


class ProductDetailView(DetailView):
    """full description of the 3d Model"""
    model = Product
    slug_field = "url"
    template_name = "product.html"



