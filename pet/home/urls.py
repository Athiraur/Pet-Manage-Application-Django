from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Homepage view
    path('user-login/', views.user_login, name='user_login'),  # User login URL
    path('admin-login/', views.admin_login, name='admin_login'),  # Admin login URL
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),  # Admin dashboard URL
    path('user-dashboard/', views.user_dashboard, name='user_dashboard'),  # User dashboard URL

    path('add-animal/', views.add_animal, name='add_animal'),
    path('animal_list/', views.animal_list, name='animal_list'),
    path('edit-animal/<int:pk>/', views.edit_animal, name='edit_animal'),
    path('delete-animal/<int:pk>/', views.delete_animal, name='delete_animal'),

    path('add-bird/', views.add_bird, name='add_bird'),
    path('bird_list/', views.bird_list, name='bird_list'),
    path('edit-bird/<int:pk>/', views.edit_bird, name='edit_bird'),
    path('delete-bird/<int:pk>/', views.delete_bird, name='delete_bird'),

    path('add-customer/', views.add_customer, name='add_customer'),
    path('customer_list/', views.customer_list, name='customer_list'),
    path('edit-customer/<int:pk>/', views.edit_customer, name='edit_customer'),
    path('delete-customer/<int:pk>/', views.delete_customer, name='delete_customer'),

    path('add-doctor/', views.add_doctor, name='add_doctor'),
    path('doctor_list/', views.doctor_list, name='doctor_list'),
    path('edit-doctor/<int:pk>/', views.edit_doctor, name='edit_doctor'),
    path('delete-doctor/<int:pk>/', views.delete_doctor, name='delete_doctor'),

    path('user-login/', views.user_login, name='user_login'),

    path('add-appoinment/', views.add_Appoinment, name='add_appoinment'),

    path('get-doctor-details/<int:doctor_id>/', views.get_doctor_details, name='get_doctor_details'),

    path('view-appoinment',views. view_appoinments,name='view_appoinment'),
    path('admin_view_appoinments',views.admin_view_appoinments,name='admin_view_appoinments')

]




 
