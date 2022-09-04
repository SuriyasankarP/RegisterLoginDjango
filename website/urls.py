from django.urls import path
from . import views

urlpatterns = [

    path('',views.join, name='home'),
    path('/',views.join, name='join'),

    path('list',views.list,name='list'),
    
]