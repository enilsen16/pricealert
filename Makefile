celery-run:
	celery -A pricealert worker -B -l info

gdax-celery:
	python gdax_celery.py

gdax-wallaroo:
	python gdax_wallaroo.py

django-runserver:
	python manage.py runserver
