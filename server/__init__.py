from __future__ import absolute_import, unicode_literals

# Asegúrate de que Celery esté importado en el inicio del proyecto
from .celery import app as celery_app

__all__ = ('celery_app',)