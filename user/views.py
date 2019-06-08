# Liberaries
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from functools import partial
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, JSONParser
import cloudinary.uploader

# Local modules.
from django.contrib.auth.models import User
from user.utility import generate_token, AllowedUserPermission
from user.serializers import UserSerializer
from user.models import Profile
from user.utility import raises_error


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (partial(AllowedUserPermission,['POST'], IsAuthenticated),)
    serializer_class = UserSerializer
    queryset = User.objects.all()
    parser_classes = (
    MultiPartParser,
    JSONParser,
    )

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
          'address': data.get('address', None),
          'image': data.get('image', None)
        }
        serializer.save(profile=profile)

    def get_upload_response(self):
        user = User.objects.get(pk=self.request.user.pk)
        serializer = self.get_serializer(user)
        return Response(serializer.data)

    @action(detail=False) 
    def destroy_upload(self, request, *args, **kwargs):
        profile = Profile.objects.get(user_id=request.user.pk)
        if profile.image:
           public_id=profile.image_public_id
           cloudinary.uploader.destroy(public_id)  
           if not kwargs.get('pass_res'):
              profile.image=""
              profile.image_public_id=""
              profile.save()
              return self.get_upload_response()

    @action(detail=False) 
    def upload(self, request, *args, **kwargs):
        file = self.request.data.get('file')
        instance = Profile.objects.get(user_id=request.user.pk)
        if instance.image:
            self.destroy_upload(request, pass_res=True)
        if file:
            upload_data = cloudinary.uploader.upload(file)
            if upload_data:
                instance.image = upload_data['url']
                instance.image_public_id = upload_data['public_id']
                instance.save()

                return self.get_upload_response()
        else:
            raises_error('file_error', 400)

            