
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from booking.template import template
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from booking.models import Booking
from booking.serializers import BookingSerializer


def task_runner():
    scheduler = BackgroundScheduler()
    scheduler.add_job(Booking_notification, 'interval', hours=5)
    scheduler.start()

def send_mail(user, booking, message):
    message = Mail(
        from_email='no-reply@flightTrip.com',
        to_emails=user.email,
        subject=message['subject'],
        html_content=template.format(message['subject'], message['title'],user.username, \
            booking['ref'], booking['flight_date'], booking['location'], booking['flight_seat'], booking['flight']['name']))
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(str(e))

def Booking_notification():
    date = datetime.today().strftime('%Y-%m-%d')
    day = int(date[-2:]) + 1
    date = date[:-2] + str(day)
    bookings = Booking.objects.filter(flight_date=date)
    count = len(bookings)
    message = {
      'title': 'Flight departure reminder',
      'subject': 'Flight departure reminder'
    }
    print('sending booking notification email to ' + str(count) + ' user/users')
    for booking in bookings:
        booking_data = BookingSerializer(booking).data
        send_mail(booking.user, booking_data, message)
