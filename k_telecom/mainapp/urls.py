from django.urls import path
from .views import main, succes

app_name = 'mainapp'

urlpatterns = [
    path('', main, name='main'),
    path('success/', succes, name='succes'),
]