from django.urls import path
from .views import main

app_name = 'mainapp'

urlpatterns = [
    path('', main, name='main'),
]