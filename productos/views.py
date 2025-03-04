from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpRequest
from .models import Producto, Sucursal
from rest_framework.response import Response
from rest_framework import status

from django.core.paginator import Paginator


 
def Home(request):
    
    lista_products = Producto.objects.all()
    lista_sucursales = Sucursal.objects.all()

    # Configura la paginación (por ejemplo, 10 productos por página)
    paginator = Paginator(lista_products, 10)
    page_number = request.GET.get('page')  # Obtén el número de página desde la URL
    products = paginator.get_page(page_number)  # Obtén la página actual

    # Pasa los productos paginados al contexto
    context = {'products': products, "lista_sucursales" : lista_sucursales}
    return render(request, 'Home.html', context)



def Home_redirect(request):
    return redirect('Home')