from django.contrib import admin
from .models import ProductoSucursal, Sucursal, ProductoVariante, Producto

# Registrar modelos en el panel de administración
admin.site.register(ProductoSucursal)
admin.site.register(Sucursal)
admin.site.register(ProductoVariante)

admin.site.register(Producto)