from django.urls import path
from . import views


urlpatterns = [
   
    path('free/', views.free),
    path('courses/', views.courses),
    path('', views.paid, name='home'),
    path('investor/', views.investor, name='investor'),
    path('success/', views.success, name='success'),
    path('form/', views.show_form, name='form'),
    path('userform/', views.usercfrom, name='registration'),
    path('login/', views.loginform, name='login'),
]
