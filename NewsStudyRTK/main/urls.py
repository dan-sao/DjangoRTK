from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('sidebar/', views.sidebar),
    path("login/", views.login, name="login"),
    path("news/", views.news_i, name="news"),
]
