# Liberaries
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

# Local modules.
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from booking.serializers import BookingSerializer
from booking.models import Booking
from flight.models import Flight
from user.utility import raises_error
from booking.utility import send_mail

class BookingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited. 
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = BookingSerializer
    
    def get_queryset(self):
        params = self.request.query_params
        flight_date = params.get('flightDate')
        user_id = params.get('userId')
        location = params.get('location')
        flight_id = params.get('flightId')
        queryset = Booking.objects.filter()
        if flight_date:
            queryset = queryset.filter(flight_date=flight_date)
        if location:
            queryset = queryset.filter(location=location) 
        if user_id:
           queryset = queryset.filter(user_id=user_id)
        if flight_id:
           queryset = queryset.filter(flight_id=flight_id)
        return queryset

    def get_available_flight(self):
        flights = Flight.objects.all()
        flight_date=self.request.data.get('flight_date')
        for flight in flights:
            bookings = Booking.objects.filter(flight_id=flight.pk, flight_date=flight_date)
            if len(bookings) < 200:
                return flight.pk
        return raises_error('not_found', 400, flight_date)

    def create(self, request):
        user = self.request.user
        request.data['user_id'] = user.id
        request.data['flight_id'] = self.get_available_flight()
        serializer = BookingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        send_mail(user,serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)