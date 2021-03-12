from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include

urlpatterns = [
    path('display_name', views.display_name, name='display_name'),
]