from django.db import models
from flight_control.user.base_model import BaseModel
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from flight_control.flight.models import Flight

import datetime

class Booking(BaseModel):
    flight_date = models.DateField(blank=False, null=False)
    flight_seat = models.CharField(max_length=255, blank=False, null=False)
    ref = models.CharField(max_length=255, default=get_random_string(length=32))
    location = models.CharField(max_length=255, blank=False, null=False)
    user = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, related_name='flights', on_delete=models.CASCADE)


    def __unicode__(self):
        return self.ref

