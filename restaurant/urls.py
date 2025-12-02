from django.urls import path, include
from . import views

app_name = 'restaurant'

urlpatterns = [
    path('home/', views.index_restaurant, name='index_restaurant'),
    path('register/', views.register_restaurant, name='register_restaurant'),
    path('login/', views.login_restaurant, name='login_restaurant'),
    path('logout/', views.logout_restaurant, name='logout_restaurant'),
]