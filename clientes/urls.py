
from django.contrib import admin
from django.urls import path, include
from .views import start
from .views import person_list
from .views import new_person
from .views import update_person
from .views import delete_person


urlpatterns = [
    path('start/', start, name='start'),
    path('person_list/', person_list, name='person_list'),
    path('new_person/', new_person, name='new_person'),
    path('update_person/<int:id>', update_person, name='update_person'),
    path('delete_person/<int:id>', delete_person, name='delete_person'),
]
