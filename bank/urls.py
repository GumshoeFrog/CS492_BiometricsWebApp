from django.urls import path, include
from . import views

app_name = 'bank'

urlpatterns = [
    path('home/', views.index_bank, name='index_bank'),
    path('register/', views.register_bank, name='register_bank'),
    path('login/', views.login_bank, name='login_bank'),
    path('logout/', views.logout_bank, name='logout_bank'),
]