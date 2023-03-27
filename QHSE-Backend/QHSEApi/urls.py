from django import views
from django.contrib import admin
from django.urls import path
from QHSEApi import views



urlpatterns = [
    path('commande', views.commandeApi),
    path('commande/<int:id>/', views.commandeApi),
    path('fiche', views.FicheApi),
    path('fiche/<int:id>/', views.FicheApi),
]
