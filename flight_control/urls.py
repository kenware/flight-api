
from django.urls import path, include, re_path
from rest_framework import routers
from django.conf.urls import handler404
from rest_framework import renderers
from rest_framework_jwt.views import obtain_jwt_token

from django.contrib import admin
from django.urls import path

# Views
from flight_control.user.views import UserViewSet
from flight_control.flight.views import FlightViewSet
from flight_control.booking.views import BookingViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, base_name='users')
router.register(r'flight', FlightViewSet, base_name='flight')
router.register(r'booking', BookingViewSet, base_name='booking')

upload = UserViewSet.as_view({
    'post': 'upload',
    'put': 'upload',
    'patch': 'upload',
    'delete': 'destroy_upload'
})

urlpatterns = [
    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'api/v1/login/', obtain_jwt_token),
    path('admin/', admin.site.urls),
    path(r'api/v1/users/upload/', upload, name='upload'),
    path(r'api/v1/', include(router.urls)),
]
