from django.urls import path
from . import views

urlpatterns = [

    path('', views.home),

    path('donations/', views.donations),

    path('collection/', views.collection),

]