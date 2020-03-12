
from django.urls import path, include
from .views import website


urlpatterns = [
    path('', website, name='website'),
]
