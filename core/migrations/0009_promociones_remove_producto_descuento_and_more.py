# Generated by Django 4.0.4 on 2022-07-02 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_producto_fecha_inicio_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promociones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField(blank=True, null=True)),
                ('fecha_termino', models.DateField(blank=True, null=True)),
                ('descuento', models.IntegerField(default=0, null=True)),
                ('id_producto', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='producto',
            name='descuento',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='fecha_inicio',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='fecha_termino',
        ),
    ]
