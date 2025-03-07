from django.test import TestCase
from .models import Imagen
# Create your tests here.


lista_products = Imagen.objects.prefetch_related('variantes').all()

for p in lista_products:  # Iteramos sobre los productos
    print(f"Producto: {p.nombre}")  # Imprime el nombre del producto
    