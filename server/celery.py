from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Asegúrate de que Django cargue las configuraciones del proyecto correctamente
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

# Crear la aplicación de Celery
app = Celery('server')

# Configuración de Celery basada en los ajustes de Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Hace que Celery busque las tareas en todas las aplicaciones de Django automáticamente
app.autodiscover_tasks()
