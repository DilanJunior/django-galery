from django.shortcuts import render, redirect
from .models import Imagen
from django.core.paginator import Paginator
from datetime import timedelta
from collections import defaultdict
from django.core.cache import cache
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)  # Para registrar errores

def Home(request):
    cache_key = "home_page_cache"  # Clave única para la caché
    cached_data = cache.get(cache_key)  # Intenta recuperar desde Redis

    if cached_data:
        logger.info("📌 Cache hit: datos obtenidos desde Redis")
        return render(request, 'Home.html', cached_data)  # Retorna datos cacheados

    logger.info("❌ Cache miss: consultando base de datos")

    # Consultamos las imágenes desde la base de datos
    list_images = Imagen.objects.all().order_by('-fecha_subida')

    # Agrupar imágenes por mes de subida
    grouped_images = dict(grouped_images)
    for imagen in list_images:
        fecha_mes = imagen.fecha_subida.strftime("%Y-%m")
        grouped_images[fecha_mes].append(imagen)

    grouped_images = [
        {'fecha_mes_perteneciente': key, 'imagenes': value}
        for key, value in grouped_images.items()
    ]

    # Configuramos paginación (10 imágenes por página)
    paginator = Paginator(list_images, 1)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    # Contexto para la plantilla
    context = {'grouped_images': grouped_images, 'products': products}

    # Guardamos en caché con un tiempo de expiración de 10 minutos
    cache.set(cache_key, context, timeout=60 * 5)  # Por ejemplo, 5 minutos


    return render(request, 'Home.html', context)





def Home_redirect(request):
    return redirect('Home')