
from django.urls import path
from . import views


app_name = 'salesite'
urlpatterns = [

    path('', views.Index.as_view(), name='index'),
    path('register/', views.RegForm.as_view(), name='register'),
    path('prices/', views.Prices.as_view(), name='prices'),
    path('fedback/', views.fedback, name='fedback'),
    path('<int:id>/', views.ShowDew.as_view(), name='showDev')

]
