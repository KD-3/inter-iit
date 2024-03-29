"""hackathon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    path('', TemplateView.as_view(template_name='frontend/index.html'), name='home'),
    path('projects', TemplateView.as_view(template_name='frontend/projects.html'), name='projects'),
    path('feedback', TemplateView.as_view(template_name='frontend/feedback.html'), name='feedback'),
    path('register', TemplateView.as_view(template_name='frontend/register-contractor.html'), name='register'),
    path('login', TemplateView.as_view(template_name='frontend/login.html'), name='login'),
    path('register-contractor', TemplateView.as_view(template_name='frontend/register-contractor.html'), name='register-contractor')

]
