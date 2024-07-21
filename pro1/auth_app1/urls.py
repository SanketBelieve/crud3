from django.urls import path 
from .views import *

urlpatterns = [
    path('sign/',signupview),
    path('login/',loginview),
    path('logout/',logoutview)
]
