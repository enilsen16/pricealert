from django.conf.urls import url

from pricealertweb.alerts import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
