celery-run:
	celery -A pricealert worker -B -l debug

gdax-celery:
	python gdax_ws.py

django-runserver:
	python manage.py runserver
