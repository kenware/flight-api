from django.apps import AppConfig


class BookingConfig(AppConfig):
    name = 'flight_control.booking'

    def ready(self):
        from flight_control.booking.tasks import task_runner
        task_runner()