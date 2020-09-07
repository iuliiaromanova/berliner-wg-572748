from django.urls import path
from . import views

urlpatterns = [
    path('', views.anzeige_list, name='anzeige_list'),
    path('anzeige/<int:pk>/', views.anzeige_detail, name='anzeige_detail'),
    path('anzeige/neue/', views.anzeige_neue, name='anzeige_neue'),
    path('anzeige/<int:pk>/edit/', views.anzeige_edit, name='anzeige_edit'),

]