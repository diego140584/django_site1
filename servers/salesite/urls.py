
from django.urls import path
from . import views


app_name = 'salesite'
urlpatterns = [

    path('', views.index, name='index'),
]
