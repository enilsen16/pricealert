from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from pricealertweb.models import Alerts
from django.views import View
from django.views.generic import CreateView, UpdateView

class AlertView(View):
    def get(self, request):
        return render(request, "pricealertweb/alerts/index.html", {})


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
