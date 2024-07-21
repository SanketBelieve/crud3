from django.urls import path 
from .views import * 

urlpatterns = [
    path('add/',add_view),
    path('show/',show_view),
    path('update/<int:pk>/',update_view),
    path('delete/<int:x>/',delete_view)
]
