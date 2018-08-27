from channels import Group
from datetime import datetime, timedelta
from django.db.models import Avg
from djmoney.money import Money
from pricealert.celery import app
from pricealertweb.models import MarketData, Alert

@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(30.0, notify_on_price.s(), name='Alert every 30')

@app.task
def notify_on_price():
    avg_price = calculate_average_price()
    alerts = get_alerts(avg_price)
    for alert in alerts:
        notify_user(alert, avg_price)
    return True

def calculate_average_price():
    # This is pretty naive but it'll work for our purposes
    avg_price = MarketData.objects.include(
        created_at__gte=datetime.now() - timedelta(seconds=30)
    ).aggregate(
        Avg('price')
    ).values()[0]
    return Money(avg_price, 'USD')

def get_alerts(avg_price):
    return Alert.objects.filter(
        price__lte=avg_price
    ).exclude(
        sent=True
    )

def notify_user(alert, avg_price):
    # We try to send an alert to the client
    # If the user isn't online they won't get the notification
    # This could be improved by sending an email if they aren't online
    Group("user-{}".format(alert.user_id)).send(
        {'text': "The current price of BTC is: %s has surpassed: %s" % (avg_price, alert.price)}, immediately=True)

    alert.sent = True
    alert.save()
