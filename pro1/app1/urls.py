from django.urls import path 
from .views import *

urlpatterns = [
    path('add/',add_player),
    path('show/',show_player),
    path('update/<int:pk>/',updateview),
    path('delete/<int:x>/',deleteview)
]
