
# Create your tests here.
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from flight_control.user.fixtures import TestFixtures
from rest_framework.test import APIClient
import mock

from django.contrib.auth.models import User
from flight_control.user.models import Profile
from flight_control.user.utility import generate_token

#mock
from flight_control.user.mocks import valid_user
base_url = 'http://127.0.0.1:8000/api/v1'

class DotDict(dict):
    def __getattr__(self, name):
       return self[name]
def upload():
    return 'image uploaded'

class UserEndpointsTests(APITestCase, TestFixtures):
    def test_create_new_user_succeeds(self):      

        url = base_url + '/users/'
        response = self.client.post(url, valid_user)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'kenney')
        self.assertEqual(response.data['last_name'], 'keny')
        self.assertEqual(response.data['email'], 'kennedy@gmail.com')
        self.assertIn('token', response.data)

    def test_create_user_with_already_existing_email_and_username_fails(self):
        
        self.new_user()
        url = base_url + '/users/'
        response = self.client.post(url, valid_user)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('username', response.data)
        self.assertEqual(response.data['username'][0], 'A user with that username already exists.')

    def test_get_user_without_token_fails(self):
        
        url = base_url + '/users/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn('detail', response.data)
        self.assertEqual(response.data['detail'], 'Authentication credentials were not provided.')

    def test_get_all_user_succeeds(self):
        
        client = APIClient()
        self.list_of_user()
        token = 'Bearer ' + self.auth_token()
        client.credentials(HTTP_AUTHORIZATION=token)
        url = base_url + '/users/'
        response = client.get(url)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data['results'], list)
        self.assertGreaterEqual(len(response.data['results']), 5)
    
    def test_update_user_succeeds(self):
        client = APIClient()
        new_user = self.new_user()

        token = 'Bearer ' + self.auth_token()
        client.credentials(HTTP_AUTHORIZATION=token) 

        url = base_url + f'/users/{new_user.id}/'
        valid_user['is_staff'] = True
        valid_user['firstName'] = 'Ejike'
        response = client.patch(url, valid_user)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'kenney')
        self.assertEqual(response.data['last_name'], 'keny')
        self.assertEqual(response.data['first_name'], 'Ejike')
        self.assertEqual(response.data['email'], 'kennedy@gmail.com')

    def test_user_user_succeeds(self):
        client = APIClient()
        new_user = self.new_user()
        token = 'Bearer ' + self.auth_token()
        client.credentials(HTTP_AUTHORIZATION=token) 

        url = base_url + f'/users/{new_user.id}/'
    
        response = client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.data, None)
    
    @mock.patch('flight_control.user.views.cloudinary')
    def test_upload_image_to_cloudinary_succeeds(self, mock_clodinary):

        client = APIClient()
        user = self.new_user()

        mock_clodinary.uploader.upload.return_value = { 'url': 'my_passport', 'public_id': 'public_id'}
        token = 'Bearer ' + generate_token(user)
        client.credentials(HTTP_AUTHORIZATION=token) 

        url = base_url + '/users/upload/'

        response = client.put(url, {'file': 'my_passport'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], user.username)
        self.assertEqual(response.data['last_name'], user.last_name)
        self.assertEqual(response.data['email'], user.email)
        self.assertEqual(response.data['profile']['image'], 'my_passport')

    @mock.patch('flight_control.user.views.cloudinary')
    def test_change_image_upload_in_cloudinary_succeeds(self, mock_clodinary):

        client = APIClient()
        user = self.new_user()
        profile = Profile.objects.get(user_id=user.id)
        profile.image = 'my_image'
        profile.save()

        mock_clodinary.uploader.upload.return_value = { 'url': 'my_passport', 'public_id': 'public_id'}
        mock_clodinary.uploader.destroy.return_value = ''
        token = 'Bearer ' + generate_token(user)
        client.credentials(HTTP_AUTHORIZATION=token) 

        url = base_url + '/users/upload/'

        response = client.put(url, {'file': 'my_passport'})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], user.username)
        self.assertEqual(response.data['last_name'], user.last_name)
        self.assertEqual(response.data['email'], user.email)
        self.assertEqual(response.data['profile']['image'], 'my_passport')

    @mock.patch('flight_control.user.views.cloudinary')
    def test_delete_image_upload_in_cloudinary_succeeds(self, mock_clodinary):

        client = APIClient()
        user = self.new_user()
        profile = Profile.objects.get(user_id=user.id)
        profile.image = 'my_image'
        profile.save()

        mock_clodinary.uploader.destroy.return_value = ''
        token = 'Bearer ' + generate_token(user)
        client.credentials(HTTP_AUTHORIZATION=token) 

        url = base_url + '/users/upload/'

        response = client.delete(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['profile']['image'], '')

    def test_get_jwt_token_with_valid_user_succeeds(self):
        user = User.objects.create(username='kenny')
        user.set_password('12345')
        user.save()
        url = base_url + '/login/'
        response = self.client.post(url, {'username': 'kenny', 'password': '12345'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'kenny')
        self.assertIsInstance(response.data['token'], str)

    


              