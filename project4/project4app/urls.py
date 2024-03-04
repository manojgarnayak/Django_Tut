from django.urls import path
from project4app.views import *

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('contact/', contact, name='contact'),
]
