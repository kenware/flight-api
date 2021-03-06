from django.db import models
from flight_control.user.base_model import BaseModel
from django.contrib.auth.models import User

import datetime

class Profile(BaseModel):
    image = models.CharField(max_length=255, blank=True, null=True)
    image_public_id = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)

    def __unicode__(self): 
        return self.country
