# Liberaries
from django.contrib.auth.models import User, Group
from flight_control.user.models import Profile
from flight_control.booking.models import Booking
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from flight_control.flight.serializers import FlightSerializer
from flight_control.user.serializers import UserSerializer


class BookingSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SerializerMethodField()
    flight = serializers.SerializerMethodField()
    flight_id = serializers.IntegerField(write_only=True)
    user_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Booking
        fields = ('id', 'flight_date', 'flight_seat','flight', 'ref', 'flight_id', 'user_id', 'user', 'location')
 
    def get_user(self, obj):
       return  UserSerializer(obj.user).data

    def get_flight(self, obj):  
        return FlightSerializer(obj.flight).data