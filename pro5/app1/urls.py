from django.urls import path 
from .views import * 

urlpatterns = [
    path('add/',add_laptop),
    path('show/',show_laptop),
    path('update/<int:pk>/',updateview),
    path('delete/<int:x>/',deleteview)
]
