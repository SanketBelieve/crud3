from django.urls import path 
from .views import * 

urlpatterns = [
    path('logout/',logoutview),
    path('login/',loginview),
    path('signup/',signupview)
]
