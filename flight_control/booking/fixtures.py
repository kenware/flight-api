
from flight_control.user.utility import generate_token
from datetime import datetime, timezone
from flight_control.user.fixtures import TestFixtures

from flight_control.flight.models import Flight
from flight_control.booking.models import Booking
from flight_control.booking.mocks import booking_data, booking_list_data

class BookingTestFixtures(TestFixtures):
    def create_new_bookings(self):
        user = self.new_user()
        flight = self.create_new_flight()
        booking = Booking.objects.create(flight_id=flight.id, user_id=user.id,\
            flight_date=booking_data['flightDate'],flight_seat=booking_data['flightSeat'],location=booking_data['location'])
        return booking

    def create_list_of_bookings(self):
        user = self.new_user()
        flight = self.create_new_flight()
        for booking_data in booking_list_data:
            Booking.objects.create(flight_id=flight.id, user_id=user.id,\
               flight_date=booking_data['flightDate'],flight_seat=booking_data['flightSeat'],location=booking_data['location'])
        return user.id

    def create_new_flight(self):
        flight = Flight.objects.create(name='emirate', tag="gdhas")
        return flight
