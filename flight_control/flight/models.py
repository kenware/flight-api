from django.db import models
from flight_control.user.base_model import BaseModel
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

import datetime

class Flight(BaseModel):
    name = models.CharField(max_length=255, blank=False, null=False)
    tag = models.CharField(max_length=255, default=get_random_string(length=20, allowed_chars='ACTG'))


    def __unicode__(self):
        return self.name

