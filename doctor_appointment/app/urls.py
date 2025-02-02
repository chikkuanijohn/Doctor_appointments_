from django.urls import path
from django.contrib.auth import views as auth_views
# from .views import contact_view
from .views import book_appointment
from . import views

urlpatterns=[
    path('',views.doctor_appointment_login),
    path('admin_home',views.admin_home),
    path('logout',views.doctor_appointment_logout),
    path('user_home',views.user_home),
    path('register/',views.register),
    path('booking/',views.booking),
    path('book_appointment', views.book_appointment),  
    path('Contact/',views.Contact),
    path('view_bookings',views.view_bookings),
    path('add_details',views.add_details),
    path('check_up_packages/',views.check_up_packages),
    path('Our_specialities/',views.Our_specialities),
    path('About/',views.About),
    path('Testimonals/',views.Testimonals),
    path('success/', views.success, name='success'),
    path('view_doc',views.view_doc),
    path('edit_details/<pid>', views.edit_details),
    path('delete_details/<pid>', views.delete_details),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # path('contact/', contact_view, name='contact'),
    path("book-appointment/", views.book_appointment, name="book_appointment"),
    path("success/", views.success, name="success"),  # Success page
    path('view_bookings/', views.view_bookings, name='view_bookings'),
]                     