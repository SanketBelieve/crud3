from django.urls import path 
from .views import * 

urlpatterns = [
    path('add/',add_employee),
    path('show/',show_employee),
    path('update/<int:pk>/',updateview),
    path('delete/<int:x>/',deleteview)
]
