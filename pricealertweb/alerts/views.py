from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from pricealertweb.models import Alerts
from django.views.generic import ListView, CreateView, UpdateView

class AlertView(ListView):
    model = Alerts
    context_object_name = 'alert_list'
    template_name = "pricealertweb/alerts/index.html"

    def get_queryset(self):
        return Alerts.objects.filter(user_id__exact=self.request.user.id)

class CreateAlertView(CreateView):
    model = Alerts
    template_name = "pricealertweb/alerts/alert_new.html"
    fields = ['price']
    success_url = "/pricealert/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateAlertView, self).form_valid(form)

class UpdateAlertView(UpdateView):
    model = Alerts
    template_name = "pricealertweb/alerts/alert_edit.html"
    fields = ['price']
    success_url = "/pricealert/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(UpdateAlertView, self).form_valid(form)
