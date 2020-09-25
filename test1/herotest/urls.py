# from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from herotest import views

urlpatterns = [
    path('index/', views.index),
    path('add_check', views.add_check),
    url(r'^add_ajax_check', views.add_ajax_check),
    path('add_return', views.add_return),
    url(r'delete/(\w+)', views.delete),
    url(r'add/', views.add),
    url(r'^addhero', views.addhero),
    url(r'^update/(\w+)', views.update),
    url(r'update_check/(\w+)', views.update_check),
    # url('', views.index),
]
