from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('registration/', views.register, name="Regitration"),
    path('registration/product', views.product, name="product"),

]