from django.urls import path 
from .views import *

urlpatterns = [
    path('signup/',signup_view),
    path('login/',login_view)
]
