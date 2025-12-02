from django.urls import path, include
from . import views

app_name = 'biometrics'

urlpatterns = [
    path('home/', views.index_biometrics, name='index-biometrics'),
]