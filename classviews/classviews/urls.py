"""
URL configuration for classviews project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('func_view', func_view, name='func_view'),
    path('class_view', class_view.as_view(), name='class_view'),
    path('func_template', func_template, name='func_template'),
    path('class_template', class_template.as_view(), name='class_template'),
    path('Template_view', Template_view.as_view(), name='Template_view'),
    path('functionbasedview', functionbasedview, name='functionbasedview'),
    path('classbasedview', classbasedview.as_view(), name='classbasedview'),
    path('formview', formviewtemplate.as_view(), name = 'formviewtemplate')
]
