# Generated by Django 4.0.4 on 2022-07-01 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_producto_precio_producto_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(default='', max_length=500),
        ),
    ]