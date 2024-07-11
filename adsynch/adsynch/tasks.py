import requests
import xml.etree.ElementTree as ET
from celery import shared_task


@shared_task
def get_usd_rate():
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    tree = ET.fromstring(response.content)
    usd_rate = tree.find(".//Valute[CharCode='USD']")
    if usd_rate is not None:
        currency_value = usd_rate.find('Value').text
        return float(currency_value.replace(',', '.'))  # Преобразуем в числовое значение
    else:
        raise ValueError('USD курс не найден')