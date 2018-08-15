from django.shortcuts import render

def index(request):
    return render(request, 'pricealertweb/alerts/index.html', {})
