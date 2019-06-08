
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from booking.template import template

def send_mail(user, booking):
    message = Mail(
        from_email='no-reply@flightTrip.com',
        to_emails=user.email,
        subject='Flight Booking successful',
        html_content=template.format(user.username, \
            booking['ref'], booking['flight_date'], booking['location'], booking['flight_seat'], booking['flight']['name']))
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(str(e))