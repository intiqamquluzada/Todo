from django.urls import path
from .views import *

app_name = 'todo'

urlpatterns = [
    path('index/', myview, name='index'),
    path('add/', add_view, name='add'),
]
