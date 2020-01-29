from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('prueba/', views.PrubaView.as_view()),
    path('lista/', views.PruebaListView.as_view()),
    path('lista-prueba/', views.ListarPrueba.as_view()),
    path('add/', views.PruebaCreateView.as_view(), name='prueba_add'),
    path(
        'resume-foundation/', 
        views.ResumeFoundationView.as_view(),
        name='resume_foundation'
    ),
    
    
    
    
    # url para entender herenica e includes
    path(
        'home1/', 
        views.HomeTemplate1View.as_view(),
        name='home1'
    ),
    path(
        'home2/', 
        views.HomeTemplate2View.as_view(),
        name='home2'
    ),
    path(
        'home3/', 
        views.HomeTemplate3View.as_view(),
        name='home3'
    ),
]
