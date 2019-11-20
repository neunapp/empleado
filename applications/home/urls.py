from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('prueba/', views.PrubaView.as_view()),
    path('lista/', views.PruebaListView.as_view()),
    path('lista-prueba/', views.ListarPrueba.as_view()),
    path('add/', views.PruebaCreateView.as_view(), name='prueba_add'),
]
