# Generated by Django 5.2.1 on 2025-06-25 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_remove_producto_cantidadproductoblue_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='PresentacionProducto',
            field=models.CharField(max_length=100),
        ),
    ]
