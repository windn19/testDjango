from datetime import date
from django.shortcuts import render
from .settings import BASE_DIR


def home(request):
    d = date.today()
    name = 'Dave'
    _contex = {'date': d, 'name': name}
    return render(request, 'home.html', _contex)
