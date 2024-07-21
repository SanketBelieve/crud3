from django.urls import path 
from .views import * 

urlpatterns = [
    path('login/',loginview),
    path('signup/',signupview),
    path('logout/',logoutview)
]
