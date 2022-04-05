
from pathlib import Path
from pickle import TRUE
from django.http import HttpResponse
from django.shortcuts import render
from .models import Match
# Create your views here.
from django.shortcuts import redirect, render
from seat.models import Seat
from row.models import Row


def index(request):
    matches = Match.objects.filter(ticket_reserve_open=True).all()

    print(matches)
    return render(request, 'match/index.html', context={
        'matches': matches
    })


def match(request, id):
    print(id)
    matches = Match.objects.filter(id=id).all()
    seats = Seat.objects.all()
    rows = Row.objects.all()
    print(match)
    return render(request, 'match/match.html', context={
        'matches': matches,
        'seats': seats,
        'rows': rows
    })
