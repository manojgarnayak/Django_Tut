from django.urls import path
from customer.views import *

urlpatterns = [
    path('home/', home, name = 'home'),
    path('contact/', contact, name='contact'),
]
