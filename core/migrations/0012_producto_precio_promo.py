# Generated by Django 4.0.4 on 2022-07-07 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_producto_estado_promocion'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='precio_promo',
            field=models.IntegerField(default=0),
        ),
    ]