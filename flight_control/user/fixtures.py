from flight_control.user.mocks import valid_user
from django.contrib.auth.models import User
from flight_control.user.models import Profile
from flight_control.user.utility import generate_token
from datetime import datetime, timezone

class TestFixtures(object):
    def new_user(self):
        user = User.objects.create(email=valid_user['email'], username=valid_user['username'], password=valid_user['password'])
        Profile.objects.create(user=user)
        return user

    def auth_token(self):
        user = User(email='kenware@gmail.com', username='kenware2', is_staff=True)
        user.save()
        token = generate_token(user)
        return token
    
    # def auth_user_token():
    #     user = User.objects.create(email='kenware@gmail.com', username='kenware2', is_staff=True)
    #     token = generate_token(user)
    #     return token, user

    def list_of_user(self):
        for n in range(5):
            user = User(email=valid_user['email'] + str(n), username=valid_user['username'] + str(n))
            user.save()
