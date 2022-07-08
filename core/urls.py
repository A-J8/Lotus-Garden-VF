import re
from unittest.mock import patch
from django import views
from django.urls import path, re_path
from .views import *
from django.conf import settings
from django.views.static import serve
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', index,name="index"),
    path('pagLoginHtml', LoginView.as_view(template_name="core/pagLoginHtml.html"), name="pagLoginHtml"),
    path('logout', LogoutView.as_view(template_name="core/index.html"), name="logout"),
    path('pagRegHtml', pagRegHtml, name="pagRegHtml"),
    path('carrito', carrito ,name="carrito"),
    path('misCompras', misCompras ,name="misCompras"),
    path('seguimientoDespacho', seguimientoDespacho ,name="seguimientoDespacho"),
    path('suscripciones', suscripciones ,name="suscripciones"),
    path('crudHtml', crudHtml ,name="crudHtml"),
    path('agregarProducto', agregarProducto ,name="agregarProducto"),
    path('registrarProducto/', registrarProducto),
    path('eliminacionProducto/<int:id>', eliminarProducto),
    path('edicionProducto/<int:id>', edicionProducto),
    path('editarProducto/', editarProducto),
    path('promociones', promociones ,name="promociones"),
    path('edicionProducto/<int:id>', edicionProducto ,name="edicionProducto"),
    path('editarDescuento/', editarDescuento ,name="agregarDescuento"),
    path('eliminarPromocion/<int:id>/<int:id_producto>', eliminarPromocion),
    path('crearDescuento', crearDescuento ,name="crearDescuento"),
    path('registrarPromocion/', registrarPromocion),
    #carrito
    path('agregar/<int:producto_id>', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>', restar_producto, name="Sub"),
    path('limpiar/', limpiar_producto, name="cls"),
    #historial
    path('crear_historial/<int:totalC>', crear_historial, name="crear_historial"),

]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    })
]