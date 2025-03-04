from django.test import TestCase
from .models import Producto
# Create your tests here.


lista_products = Producto.objects.prefetch_related('variantes').all()

for p in lista_products:  # Iteramos sobre los productos
    print(f"Producto: {p.nombre}")  # Imprime el nombre del producto
    for p_v in p.variantes.all():  # Accedemos a las variantes relacionadas
        print(f" - Color: {p_v.color}")  # Imprime el color de cada variante
