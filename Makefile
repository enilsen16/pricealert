.PHONY: run-on-celery wallaroo celery-run gdax-celery gdax-wallaroo django-wallaroo-runserver django-celery-runserver gdax-wallaroo-receiver start-redis

setup: setup-envs

setup-envs:
	(virtualenv -p `which python2` &&\
		(. ./.env/bin/activate && pip install -r requirements.txt))

run-on-celery: start-redis gdax-celery celery-run django-celery-runserver

run-on-wallaroo: start-redis celery-run \
	gdax-wallaroo-receiver run-machida gdax-wallaroo django-wallaroo-runserver

run-machida:
	machida --application-module coinbase  --in 127.0.0.1:7000,127.0.0.1:7001 \
  --out 127.0.0.1:5555 --metrics 127.0.0.1:5001 --control 127.0.0.1:6000 \
  --data 127.0.0.1:6001 --name worker-name --external 127.0.0.1:5050 \
  --cluster-initializer --ponythreads=1 --ponynoblock >logs/machida.log 2>&1 &

celery-run:
	WITH_WALLAROO=False celery -A pricealert worker -B -l info >logs/celery.log 2>&1 &

gdax-celery:
	python gdax_celery.py

gdax-wallaroo:
	python gdax_wallaroo.py >logs/wallaroo.log 2>&1 &

django-wallaroo-runserver:
	WITH_WALLAROO=True python manage.py runserver

django-celery-runserver:
	WITH_WALLAROO=False python manage.py runserver

gdax-wallaroo-receiver:
	python gdax_wallaroo_receiver.py >logs/reciever.log 2>&1 &

start-redis:
ifneq ($(shell redis-cli ping), PONG)
	redis-server >logs/redis.log 2>&1 &
endif
