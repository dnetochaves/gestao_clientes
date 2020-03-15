
from django.contrib import admin
from django.urls import path, include
from .views import start
from .views import person_list
from .views import new_person
from .views import update_person
from .views import delete_person
from .views import DocsList, DocsDetail, DocsCreate, DocsUpdate, DocsDelete


urlpatterns = [
    path('start/', start, name='start'),
    path('person_list/', person_list, name='person_list'),
    path('new_person/', new_person, name='new_person'),
    path('update_person/<int:id>', update_person, name='update_person'),
    path('delete_person/<int:id>', delete_person, name='delete_person'),
    path('docs_list', DocsList.as_view(), name='docs_list'),
    path('docs_detail/<int:pk>/', DocsDetail.as_view(), name='docs_detail'),
    path('docs_create', DocsCreate.as_view(), name='docs_create'),
    path('docs_update/<int:pk>/', DocsUpdate.as_view(), name='docs_update'),
    path('docs_delete/<int:pk>/', DocsDelete.as_view(), name='docs_delete'),
]
