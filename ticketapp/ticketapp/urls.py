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
from match.models import Match
from django.contrib import admin
from django.urls import path
from django.core.serializers import serialize

from django.shortcuts import render

from game.models import Game


def home(request):
    context = {}
    set = Game.objects.prefetch_related('serieses').all()
    for game in set:
        series = game.serieses.all()
        print(series)
    context['games'] = set

    matches = Match.objects.prefetch_related('series', 'series__game').all()
    context['matches'] = matches
    return render(request, 'index.html', context=context)

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
]
