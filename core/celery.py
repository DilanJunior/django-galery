from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Establece el módulo de configuración predeterminado de Django para el proyecto
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

# Usar una cadena para no tener que serializar el objeto cuando Django se reinicie
app.config_from_object('django.conf:settings', namespace='CELERY')

# Cargar tareas de todas las aplicaciones registradas en Django
app.autodiscover_tasks()



@app.task(bind=True, ignore_result=True)
def example_task(self):
    print("You've triggered the example task!")