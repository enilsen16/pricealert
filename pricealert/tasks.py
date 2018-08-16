from celery.schedules import crontab
from pricealert.celery import app
from .models import Alert

@app.task
def calculate_average_price():
    # This is pretty naive but it'll work for our purposes
