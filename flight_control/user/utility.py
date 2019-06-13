from rest_framework_jwt.settings import api_settings
from rest_framework import permissions
from rest_framework.request import Request
from rest_framework import serializers
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from flight_control.user.constants import error_messages

def validate_password(value):  
   if len(value)<4 or not value:
       raises('password_error', 400)

class AllowedUserPermission(permissions.BasePermission):
    """
    Global permission check for the application. 
    """
    def __init__(self, methods, permissions_class):
        self.methods = methods
        self.permissions_class = permissions_class

    def has_permission(self, request, view):
        if request.method in self.methods:
            return True
        return self.permissions_class.has_permission(self, request, view)

class StaffAuthenticatedPermission(permissions.BasePermission):
    """
    Global permission check for the application.
    """

    def has_permission(self, request, view):
        return (request.user.is_staff or request.user.is_superuser)

class AdminAuthenticatedPermission(permissions.BasePermission):
    """
    Global permission check for the application.
    """

    def has_permission(self, request, view):
        return request.user.is_superuser


def generate_token(user):
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

    payload = jwt_payload_handler(user)
    token = jwt_encode_handler(payload)
    return token

def validate_email(value):
    user = User.objects.filter(email=value)
    if user:
        raises_error('exist', 400, 'Email')
    return value

def get_or_404(model, id):
    exist = model.objects.filter(pk=id)
    if not exist:
        raises('not_found', 404)

def custom_get_object_or_404(model, id):
    objects = model.objects.filter(pk=id).first()
    if not objects:
        raises_error('object_not_found', 404, model.__name__)
    return objects

def raises_error(error_key, status_code, *args, **kwargs):
    """
    Raises a serialization error

    Parameters:
        error_key (str): the key for accessing the correct error message
        args (*): variable number of arguments
        kwargs (**): variable number of keyword arguments
    """

    raise serializers.ValidationError({
         'message': error_messages[error_key].format(*args, **kwargs),
         'status': 'error'}, status_code)

def raises(error_key, status_code, *args, **kwargs):
    """
    Raises a serialization error

    Parameters:
        error_key (str): the key for accessing the correct error message
        args (*): variable number of arguments
        kwargs (**): variable number of keyword arguments
    """

    raise serializers.ValidationError(
         error_messages[error_key].format(*args, **kwargs),
         status_code)