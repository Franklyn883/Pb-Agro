from django.urls import path
from . import views


app_name = 'farmreach'

urlpatterns = [
    path('', views.home),
]