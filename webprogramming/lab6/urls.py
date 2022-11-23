from django.urls import re_path
from lab6 import views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^about', views.about, name='about'),
    re_path(r'^contact', views.about, name='about'),
    re_path(r'^show', views.about, name='about'),
]