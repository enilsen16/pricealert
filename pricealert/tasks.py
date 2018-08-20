from .models import MarketData, Alert
from celery.schedules import crontab
from datetime import datetime
from django.db.models import Avg
from pricealert.celery import app

@app.task
def calculate_average_price():
    # This is pretty naive but it'll work for our purposes
    return MarketData.objects.exclude(
        created_at__lte=datetime.datetime.now() - datetime.timedelta(minutes=10)
    ).aggregate(
        Avg('price')
    )

