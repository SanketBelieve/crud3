from django.urls import path 
from .views import * 

urlpatterns = [
    path('add/',addview),
    path('show/',showview),
    path('delete/<int:x>',deleteview),
    path('updateview/<int:pk>/',updateview)
]
