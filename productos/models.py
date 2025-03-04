from django.db import models

COLORES_PRIMARIOS = [
    ('Red', 'Rojo'),
    ('Blue', 'Azul'),
    ('Yellow', 'Amarillo')
]


# Modelo Producto
class Producto(models.Model):
    nombre = models.CharField(max_length=300)
    imagen = models.ImageField(upload_to="productos/", null=True, blank=False)
    descripcion = models.TextField(max_length=500)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descuento = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50, default='Activo', choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')])
    
    def precio_descuento(self):
        if self.descuento:  # Evita errores si el descuento es None
            return self.precio - (self.precio * self.descuento / 100)
        return self.precio  # Si no hay descuento, el precio no cambia


    def __str__(self):
        return self.nombre


# Modelo ProductoVariante
class ProductoVariante(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='variantes')
    cantidad = models.PositiveIntegerField()
    tallas = models.CharField(max_length=255, null=True, blank=True)  # Ejemplo: 'S,M,L,XL'
    imagen_url = models.URLField(max_length=200, null=True, blank=True)
    color = models.CharField(max_length=50, choices=COLORES_PRIMARIOS, null=True)

    def __str__(self):
        return f"Variante de {self.producto.nombre}"


# Modelo Sucursales
class Sucursal(models.Model):
    nombre_canton = models.CharField(max_length=300)
    direccion = models.CharField(max_length=255)
    contacto = models.CharField(max_length=25)
    estado = models.CharField(max_length=50, default='Activo', choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')])

    def __str__(self):
        return self.nombre_canton


""" # Modelo ProductoSucursal
class ProductoSucursal(models.Model):
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name='productos_sucursal')
    variante = models.ForeignKey(ProductoVariante, on_delete=models.CASCADE, related_name='sucursales')
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.variante.producto.nombre} en {self.sucursal.nombre_canton}" """
