from datetime import datetime
from django.shortcuts import redirect, render
from numpy import product
from .models import Producto
from .models import *
from .models import Promocion
from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate, login
from.forms import RegistroForm
from email import message
from pyexpat.errors import messages
from django.contrib import messages

# Create your views here.

def index(request):
    contexto = {'productos' : Producto.objects.all()}
    return render(request, 'core/index.html', contexto)

def pagLoginHtml(request):
    return render(request, 'core/pagLoginHtml.html')

def pagRegHtml(request):
    data = {
        'form': RegistroForm()
    }
    
    if request.method == 'POST':
        formulario = RegistroForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)      
            messages.success(request, "Registrado correctamente")     
            return redirect(to='index')
        data["form"] = formulario

    return render(request, 'core/pagRegHtml.html', data)

def carrito(request):
    return render(request, 'core/carrito.html')

def misCompras(request):
    contexto = {'historial' : Historial.objects.all()}
    return render(request, 'core/Mis_compras_1.html', contexto)    

def seguimientoDespacho(request):
    return render(request, 'core/Seguimiento_despacho.html')

def suscripciones(request):
    return render(request, 'core/sus.html')  

def crudHtml(request):
    contexto = {'productos' : Producto.objects.all()}
    return render(request, 'core/crudHtml.html', contexto)    

def crearDescuento(request):    
    return render(request, 'core/crearDescuento.html')

def agregarProducto(request):
    return render(request, 'core/AgregarProducto.html')



def registrarProducto(request):
    nombre = request.POST['nombreP']
    precio = request.POST['precio']
    stock = request.POST['stock']
    imagen = request.POST['imagen']
    descripcion = request.POST['descripcion']

    poducto = Producto.objects.create(nombre=nombre,precio=precio,stock=stock,
    imagen=imagen,descripcion=descripcion)
    messages.success(request, "añadido")
    return redirect('crudHtml')

def eliminarProducto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    messages.success(request, "eliminado")
    return redirect('crudHtml')

def edicionProducto(request, id):
    producto = Producto.objects.get(id=id)
    data = {
        'titulo': 'Edicion de producto',
        'producto': producto
    }
    messages.success(request, "editado")
    return render(request, "core/edicionProducto.html", data)


def editarProducto(request):
    id = int(request.POST['id']) 
    nombre = request.POST['nombreP']
    precio = request.POST['precio']
    stock = request.POST['stock']
    imagen = request.POST['imagen']
    descripcion = request.POST['descripcion']

    producto = Producto.objects.get(id=id)
    producto.nombre = nombre
    producto.precio = precio
    producto.stock = stock
    producto.imagen = imagen
    producto.descripcion = descripcion
    producto.save()
    messages.success(request, "editado")
    return redirect('crudHtml')

def promociones(request):
     contexto = {'promociones' : Promocion.objects.all()}
     return render(request, 'core/crudPromHtml.html', contexto)    


def edicionProducto(request, id):
    promocion = Promocion.objects.get(id=id)
    data = {
        'titulo': 'Edicion de producto',
        'promocion': promocion
    }
    return render(request, 'core/agregarDesc.html',data)

def editarDescuento(request):
    id = int(request.POST['id']) 
    idProducto = int(request.POST['idProducto']) 
    descuento = request.POST['descuento']  
    fecha_inicio = request.POST.get('fechaIni')
    fecha_termino =request.POST.get('fechaTerm')
    promocion = Promocion.objects.get(id=id)
    promocion.id = id
    promocion.id_producto = idProducto
    promocion.descuento = descuento
    promocion.fecha_inicio = fecha_inicio
    promocion.fecha_termino = fecha_termino
    promocion.save()
    
    messages.success(request, "editado")
    return redirect('promociones')

def eliminarPromocion(request, id, id_producto):
    promocion = Promocion.objects.get(id=id)
    producto = Producto.objects.get(id=id_producto)
    producto.estado_promocion = False
    producto.precio = producto.precio_antiguo
    producto.precio_antiguo = 0
    producto.save()  
    promocion.delete()
   
    messages.success(request, "eliminado")
    return redirect('promociones')

def registrarPromocion(request):
    id_producto = int(request.POST['idProducto']) 
    descuento = int(request.POST['descuento'])  
    fecha_inicio = request.POST.get('fechaIni')
    fecha_termino =request.POST.get('fechaTerm')

    promocion = Promocion.objects.create(id_producto=id_producto,descuento=descuento,fecha_termino=fecha_termino,
    fecha_inicio=fecha_inicio)

    producto = Producto.objects.get(id=id_producto)
    producto.estado_promocion = True
    producto.precio_antiguo = producto.precio
    producto.precio = (producto.precio * (int(request.POST['descuento']))/100)
    producto.save()
    
    messages.success(request, "añadido")
    return redirect('promociones')


########Carrito
from django.shortcuts import redirect, render
from core.Carrito import Carrito

from core.models import Producto

# Create your views here.


def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    if producto.stock > 0:
        producto.stock -= 1
        producto.save()
        carrito.agregar(producto) 
    return redirect("carrito")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("carrito")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    if producto.stock >= 0:
        producto.stock += 1
        producto.save()
        carrito.restar(producto)
    return redirect("carrito")

def limpiar_producto(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("carrito")

#para historial
def crear_historial(request, totalC):
    total = totalC
    fecha = datetime.now()
    historial = Historial.objects.create(fecha=fecha,total=total)
    messages.success(request, "Gracias por su compra!")
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect('carrito')


   