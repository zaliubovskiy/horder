import datetime
from django.db import models


# Create your products here.
from django.urls import reverse


class Category(models.Model):

    name = models.CharField("Name", max_length=100)
    url = models.SlugField(max_length=100, unique=True)
    image = models.ImageField("Image", upload_to="categories/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class SubCategory(models.Model):

    name = models.CharField("Name", max_length=100)
    url = models.SlugField(max_length=100, unique=True)
    image = models.ImageField("Image", upload_to="categories/")
    parent = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "SubCategory"
        verbose_name_plural = "SubCategories"


class Product(models.Model):

    name = models.CharField("Name", max_length=40)
    image = models.CharField("Image", max_length=255)
    download_link = models.CharField("Download link", max_length=500, null=True, )
    description = models.TextField("Description", null=True, blank=True, max_length=1000)
    category = models.ManyToManyField("SubCategory", verbose_name="categories")
    date_uploaded = models.DateField("Upload date", default=datetime.date.today)
    url = models.SlugField(max_length=100, unique=True)
    colors = models.ManyToManyField("Color", verbose_name="colors")
    materials = models.ManyToManyField("Material", verbose_name="materials")
    brand = models.ManyToManyField("Brand", verbose_name='brands', blank=True)
    style = models.ManyToManyField("Style", verbose_name="styles", blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "3d model"
        verbose_name_plural = "3d models"


class Color(models.Model):

    name = models.CharField("Name", max_length=255)
    link = models.CharField("Link", max_length=255)
    hex_html = models.CharField("HEX code", max_length=6, default="000000")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Color"
        verbose_name_plural = "Colors"


class Material(models.Model):
    name = models.CharField("Name", max_length=255)
    image = models.ImageField("Image", upload_to="materials/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materials"


class Brand(models.Model):
    name = models.CharField("Name", max_length=255)
    image = models.ImageField("Image", upload_to="brands/")
    link = models.CharField("Link", max_length=255)
    description = models.TextField("Description", null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"


class Style(models.Model):
    name = models.CharField("Name", max_length=255)
    description = models.TextField("Description", null=True)

    def __str__(self):
        return self.name

