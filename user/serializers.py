# Liberaries
from django.contrib.auth.models import User, Group
from user.models import Profile
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

# local modules
from .utility import generate_token, validate_password, validate_email

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('country', 'city', 'address', 'image')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = ProfileSerializer(required=False)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password','profile')

    def validate_password(self, value):
        validate_password(value)
        return make_password(value)
    
    def create(self, validated_data):
        email = validated_data.get('email')
        validate_email(email)
        user = User.objects.create(**validated_data)
        Profile.objects.create(user=user)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()

        profile.country = profile_data.get('country', profile.country)
        profile.city = profile_data.get('city', profile.city)
        profile.address = profile_data.get('address', profile.address)
        profile.image = profile_data.get('image', profile.image)
        profile.save()
        return instance 


