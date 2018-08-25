from .models import MarketData, Alert
from celery.schedules import crontab
from datetime import datetime
from django.db.models import Avg
from pricealert.celery import app

# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     sender.add_periodic_task(30.0, notify_on_price.s(), name='Alert every 30')

# @app.task
def notify_on_price():
    avg_price = calculate_average_price()
    alerts = get_alerts(avg_price)
    # Get users to send alert to
    # call an alert for each group

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
