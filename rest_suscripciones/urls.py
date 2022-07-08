from django.urls import path
from rest_suscripciones.views import lista_suscripciones, detalle_suscripcion

urlpatterns =[
    path('lista_suscripciones', lista_suscripciones, name="lista_suscripciones"),
    path('detalle_suscripcion/<id>', detalle_suscripcion, name="detalle_suscripcion"),
]