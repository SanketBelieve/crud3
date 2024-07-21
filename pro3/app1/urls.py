from django.urls import path
from .views import *

urlpatterns = [
    path('add/',add_student),
    path('show/',show_student),
    path('update/<int:pk>/',update_student),
    path('delete/<int:x>/',deleteview)
]
