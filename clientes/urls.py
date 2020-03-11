
from django.contrib import admin
from django.urls import path, include
from .views import start


urlpatterns = [
    path('start/', start, name='start'),
]
