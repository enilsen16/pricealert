celery-run:
	celery -A pricealert beat
	
coinbase-run:
	python gdax_ws.py

django-runserver:
	python manage.py runserver
