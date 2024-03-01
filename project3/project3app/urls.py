from django.urls import path
from project3app.views import *

urlpatterns = [
    path('home/', home, name='home'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('contact-us/', contactus, name='contact-us')
]
