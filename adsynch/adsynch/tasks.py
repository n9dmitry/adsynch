# adsynch/tasks.py
# from __future__ import absolute_import, unicode_literals
from xml import etree

from celery import shared_task
import requests
from .celery import app
import xml.etree.ElementTree as ET

@shared_task
def get_usd_rate():
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    tree = ET.fromstring(response.content)
    usd_rate = tree.find(".//Valute[CharCode='USD']")
    if usd_rate is not None:
        currency_value = usd_rate.find('Value').text
        return float(currency_value.replace(',', '.'))  # Преобразуем в числовое значение

    else:
        raise ValueError('USD rate not found in the response')
