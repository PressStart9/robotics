from django.urls import path
from . import views
from django.views.generic import ListView, DetailView

urlpatterns = [
    path(r'', views.view_main, name='view_main'),
    path(r'news/', views.view_news, name='view_news'),
    path(r'contacts/', views.view_contacts, name='view_contacts'),
]