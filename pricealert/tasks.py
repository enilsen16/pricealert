from .models import MarketData, Alert
from celery.schedules import crontab
from datetime import datetime
from django.db.models import Avg
from pricealert.celery import app

# @app.task
def notify_on_price():
    avg_price = calculate_average_price()
    alerts = get_alerts(avg_price)
    # Call notify 

def calculate_average_price():
    # This is pretty naive but it'll work for our purposes
    return MarketData.objects.exclude(
        created_at__lte=datetime.datetime.now() - datetime.timedelta(minutes=10)
    ).aggregate(
        Avg('price')
    )

def get_alerts(avg_price):
    return Alert.objects.filter(
        price__lte=avg_price
    ).exclude(
        alert_sent=True
    )
