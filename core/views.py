from django.shortcuts import render
import requests

from core.models import Event


# Create your views here.
def index(request):
    events = Event.objects.all().order_by('pk')

    data = {
        'title': 'Главная страница',
        'events': events
    }
    return render(request, 'index.html', context=data)