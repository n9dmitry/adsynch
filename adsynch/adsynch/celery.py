from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Задаем настройки Django для Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'adsynch.settings')

# Создаем экземпляр Celery
app = Celery('adsynch')

# Загружаем конфигурацию из файла настроек Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически обнаруживаем задачи (tasks) в приложениях Django
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')