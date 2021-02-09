from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import ListView, DetailView

urlpatterns = [
    path(r'', views.view_main, name='view_main'),
    path(r'news/', views.view_news, name='view_news'),
    path(r'schedule/', views.view_schedule, name='view_schedule'),
    path(r'invents/', views.view_invents, name='view_invents'),
]