from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('customer', views.cust, name='cust'),
    path('custtable', views.custtable, name='custtable'),
    path('dealer', views.dealer, name='dealer'),
    path('dealertable', views.dealertable, name='dealeartable')


]