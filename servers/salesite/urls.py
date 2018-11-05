
from django.urls import path
from . import views


app_name = 'salesite'
urlpatterns = [

    path('', views.Index.as_view(), name='index'),
    path('register/', views.regForm, name='register'),
    path('prices_template/', views.PricesTemplate.as_view(), name='pricestemplate'),
    path('fedback/', views.Fedback.as_view(), name='fedback'),
    path('<int:id>/', views.ShowDew.as_view(), name='showDev'),
    path("prices_laptop/", views.PricesLaptop.as_view(), name='priceslaptop'),

]
