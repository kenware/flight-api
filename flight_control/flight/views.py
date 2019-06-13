# Liberaries
from rest_framework import viewsets

# Local modules.
from django.contrib.auth.models import User
from flight_control.user.utility import AdminAuthenticatedPermission
from flight_control.flight.serializers import FlightSerializer
from flight_control.flight.models import Flight


class FlightViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (AdminAuthenticatedPermission,)
    serializer_class = FlightSerializer
    queryset = Flight.objects.all()
