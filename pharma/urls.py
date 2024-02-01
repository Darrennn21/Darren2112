from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="homepage"),
    
    
    path("emptable/", views.emptable, name="emptable"),
    path('employees/add/', views.add_employee, name='add_employee'),
    path('employees/<int:pk>/', views.edit_employee, name='edit_employee'),
    path('delete_employee/<int:employee_id>/', views.delete_employee, name='delete_employee'),
     
    path('dealertable/', views.dealertable, name='dealertable'),
    path("dealerforminsert/", views.dealerforminsert, name="dealerforminsert"),
    path('dealer/<int:pk>/edit/', views.edit_dealer, name='edit_dealer'),
    path('delete_dealer/<int:dealer_id>/', views.delete_dealer, name='delete_dealer'),
    
    path("medtable/", views.medtable, name="medtable"),
    path('medAdd/', views.medAdd, name="medAdd"), 
    path('medicine/<int:pk>/', views.edit_medicine, name='edit_medicine'),
    path('delete_medicine/<int:medicine_id>/', views.delete_medicine, name='delete_medicine'),

    path('customers/', views.customer_list, name='customer_list'),
    path('edit_customer/<int:customer_id>/', views.edit_customer, name='edit_customer'),
    path('delete_customer/<int:customer_id>/', views.delete_customer, name='delete_customer'),
    path('add_customer/', views.add_customer, name='add_customer'),
    
    path('purchase_table/', views.purchase_table, name='purchase_table'),
    path('add_purchase/', views.add_purchase, name='add_purchase'),
    path('edit_purchase/<int:pk>/', views.edit_purchase, name='edit_purchase'),
    path('delete_purchase/<int:pk>/', views.delete_purchase, name='delete_purchase'),
]
