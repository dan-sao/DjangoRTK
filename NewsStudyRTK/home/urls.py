from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name='demo'),
    # path('about/', views.about, name='about'),
    # path('contacts/', views.contacts, name='contacts'),
    # path('sidebar/', views.sidebar),
]
