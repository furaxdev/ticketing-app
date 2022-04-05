"""ticketapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import include, path
from django.shortcuts import redirect, render

from game.models import Game


def home(request):

    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about/about.html')


def contact(request):
    return render(request, 'contact/contact.html')


def register(request):
    return render(request, 'register.html', {})


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name="contact"),

    path('matches/', include('match.urls')),
    path('auth/', include('user.urls')),
    path('admin/', admin.site.urls),
]
