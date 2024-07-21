from django.urls import path 
from .views import * 

urlpatterns = [
    path('signup/',signupview),
    path('login/',loginview),
    path('logout/',logoutview)
]
