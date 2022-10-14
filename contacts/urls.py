from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'yield'
urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('addpersonne/', views.addpersonne, name='addpersonne'),
    path('uploadCsv/', views.uploadCsv, name='uploadCsv'),
    path('cjson/', views.serveJson, name='cjson'),
]