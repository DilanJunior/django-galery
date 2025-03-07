from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from .views import Home, Home_redirect, test_redis_cache

urlpatterns = [ path('store/', Home, name='Home'),
                path('', Home_redirect, name="Home_redirect"),
                path('test-redis-cache/', test_redis_cache, name='test_redis_cache'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)