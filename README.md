# pricealert

This is an application designed to show the difference between batch processing and stream processing. If you aren't familiar with either Batch or Stream processing there are good articles online. Many of the use-cases where you'd normally use batch processing are perfect use-cases for streaming.

In this application we use [Celery](http://docs.celeryproject.org/en/latest/index.html) to run our periodic tasks. We're going to use Wallaroo 0.5.2 do demonstrate taking our celery logic and converting it to Wallaroo. 
