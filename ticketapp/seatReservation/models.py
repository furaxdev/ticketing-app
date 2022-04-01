from tkinter import CASCADE
from django.db import models

from match.models import Match
from django.contrib.auth.models import User

from seat.models import Seat
# Create your models here.


class SeatReservation(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
