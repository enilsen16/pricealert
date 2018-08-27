from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from pricealertweb.models import Alert, MarketData
from django.views.generic import ListView, CreateView, UpdateView

class AlertView(ListView):
    model = Alert
    context_object_name = 'alert_list'
    template_name = "pricealertweb/alert/index.html"

    def get_queryset(self):
        return Alert.objects.filter(user_id__exact=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super(AlertView, self).get_context_data(**kwargs)
        context['last_price'] = MarketData.objects.last().price
        return context

class CreateAlertView(CreateView):
    model = Alert
    template_name = "pricealertweb/alert/alert_new.html"
    fields = ['price']
    success_url = "/pricealert/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateAlertView, self).form_valid(form)

class UpdateAlertView(UpdateView):
    model = Alert
    template_name = "pricealertweb/alert/alert_edit.html"
    fields = ['price']
    success_url = "/pricealert/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(UpdateAlertView, self).form_valid(form)
