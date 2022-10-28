from django.contrib import admin
from django.urls import path
from django.urls import re_path
from firstapp import views

urlpatterns = [
    re_path(r'^product/(?P<productId>\d+)/', views.product),
    re_path(r'^product/$', views.product),
    re_path(r'^user/(?P<id>\d+)/(?P<name>\d+)', views.user),
    path('', views.index, name="home"),
    path('about/', views.about),
    re_path(r'^contact', views.contact),
    path('admin/', admin.site.urls),
]
