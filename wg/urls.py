from django.urls import path
from . import views

urlpatterns = [
    path('', views.anzeige_list, name='anzeige_list'),
]