from django.shortcuts import render, redirect
from .models import Imagen
from django.core.paginator import Paginator
from datetime import timedelta
from collections import defaultdict
from django.core.cache import cache
from django.http import HttpResponse
import logging
logger = logging.getLogger(__name__)


def test_redis_cache(request):
    try:
        # Intenta almacenar un valor en Redis
        cache.set('my_key', 'hello_redis', timeout=60 * 15)  # Se cachea por 15 minutos

        # Intenta recuperar el valor
        value = cache.get('my_key')

        if value:
            return HttpResponse(f'Cache hit: {value}')
        else:
            return HttpResponse('Cache miss')
    except Exception as e:
        logger.error(f"Error de caché: {e}")
        return HttpResponse(f"Error: {str(e)}", status=500)

# [07/Mar/2025 00:49:20] "GET /test-redis-cache/ HTTP/1.1" 500 145
 
def Home(request):
    
    list_images = Imagen.objects.all().order_by('-fecha_subida')

    # Agrupar imágenes por fecha y calcular la fecha final
    grouped_images = defaultdict(list)
    for imagen in list_images:
        fecha_mes = imagen.fecha_subida.strftime("%Y-%m")  # Formato YYYY-MM
        grouped_images[fecha_mes].append(imagen)

    # Convertir a lista de diccionarios para el template
    grouped_images = [
        {'fecha_mes_perteneciente': key, 'imagenes': value}
        for key, value in grouped_images.items()
    ]
   
    # Configura la paginación (por ejemplo, 10 productos por página)
    paginator = Paginator(list_images, 10)
    page_number = request.GET.get('page')  # Obtén el número de página desde la URL
    products = paginator.get_page(page_number)  # Obtén la página actual

    # Pasa los productos paginados al contexto
    context = {'grouped_images': grouped_images}
    return render(request, 'Home.html', context)




def Home_redirect(request):
    return redirect('Home')