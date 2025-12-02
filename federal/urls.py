from django.urls import path, include
from . import views

app_name = 'federal'

urlpatterns = [
    path('home/', views.index_federal, name='index_federal'),
    path('register/', views.register_federal, name='register_federal'),
    path('login/', views.login_federal, name='login_federal'),
    path('logout/', views.logout_federal, name='logout_federal'),
]