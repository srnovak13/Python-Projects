from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    namelist = ['John Smith', 'Pocahontas', 'Ben Franklin', 'George Washington', 'Thomas Jefferson']
    context = {
        'names': namelist
    }
    return render(request, "home.html", context)
