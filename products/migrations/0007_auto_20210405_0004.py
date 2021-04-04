# Generated by Django 3.0.3 on 2021-04-04 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20210404_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='style',
            field=models.ManyToManyField(blank=True, to='products.Style', verbose_name='styles'),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ManyToManyField(blank=True, to='products.Brand', verbose_name='brands'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.CharField(max_length=255, verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=40, verbose_name='Name'),
        ),
    ]
