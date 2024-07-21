from django.urls import path 
from .views import *

urlpatterns = [
    path('add/',add_mobile),
    path('show/',show_mobile),
    path('update/<int:pk>/',update_mobile),
    path('delete/<int:x>/',delete_mobile)
]
