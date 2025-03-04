from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from .views import Home, Home_redirect

urlpatterns = [ path('store/', Home, name='Home'),
                path('', Home_redirect, name="Home_redirect")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)