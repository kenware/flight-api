# Liberaries
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from functools import partial

# Local modules.
from django.contrib.auth.models import User
from user.utility import generate_token, AllowedUserPermission
from user.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # permission_classes = (partial(AllowedUserPermission,['POST'], IsAuthenticated),)
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request):

        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = generate_token(user)
        serializer = UserSerializer(user)
        user_data = serializer.data
        user_data['token'] = token
        return Response(user_data)
    
    def perform_update(self, serializer):
        data = self.request.data
        profile = {
          'country': data.get('country', None),
          'city': data.get('city', None),
          'address': data.get('address', None)
        }
        serializer.save(profile=profile)
