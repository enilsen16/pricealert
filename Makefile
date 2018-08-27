celery-run:
	celery -A pricealert worker -B -l debug 

coinbase-run:
	python gdax_ws.py

django-runserver:
	python manage.py runserver
