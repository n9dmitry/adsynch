from __future__ import absolute_import, unicode_literals

# Импортируем Celery app
from .celery import app as celery_app

# Устанавливаем Celery app как атрибут модуля
__all__ = ('celery_app',)