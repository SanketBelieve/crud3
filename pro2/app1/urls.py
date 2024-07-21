from django.urls import path 
from .views import * 

urlpatterns = [
    path('add/',add_person),
    path('show/',show_person),
    path('update/<int:pk>/',updateview),
    path('delete/<int:x>/',deleteview)
]
