
# Create your tests here.
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from flight_control.user.fixtures import TestFixtures
from flight_control.booking.fixtures import BookingTestFixtures
from rest_framework.test import APIClient
import mock
from django.contrib.auth.models import User
from flight_control.booking.mocks import get_date

#mock
from flight_control.booking.mocks import booking_data, booking_list_data

base_url = 'http://127.0.0.1:8000/api/v1'
client = APIClient()

class UserEndpointsTests(APITestCase, BookingTestFixtures):
    @mock.patch('flight_control.booking.views.send_mail')
    def test_create_new_booking_succeeds(self, mock_send_email_to_user_func):     
        self.create_new_flight()

        url = base_url + '/booking/'
        token = 'Bearer ' + self.auth_token()
        client.credentials(HTTP_AUTHORIZATION=token)
        response = client.post(url, booking_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['flight_date'], booking_data['flightDate'])
        self.assertEqual(response.data['flight_seat'],  booking_data['flightSeat'])
        self.assertEqual(response.data['location'], booking_data['location'])
    
    @mock.patch('flight_control.booking.views.send_mail')
    def test_create_new_booking_with_no_flight_schedule_fails(self, mock_send_email_to_user_func):     

        url = base_url + '/booking/'
        token = 'Bearer ' + self.auth_token()
        client.credentials(HTTP_AUTHORIZATION=token)
        response = client.post(url, booking_data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_all_user_bookings_without_token_fails(self):
        
        url = base_url + '/booking/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn('detail', response.data)
        self.assertEqual(response.data['detail'], 'Authentication credentials were not provided.')

    def test_filter_booking_with_and_date_and_location_succeeds(self):
        self.create_list_of_bookings

        query = f'?date={get_date()}&location={booking_list_data[0]["location"]}'
        url = base_url + '/booking/' + query
        
        token = 'Bearer ' + self.auth_token()
        client.credentials(HTTP_AUTHORIZATION=token)
        response = client.get(url)

        self.assertIsInstance(response.data['results'], list)
        self.assertIsInstance(response.data, dict)
        self.assertGreaterEqual(len(response.data), 1)




              