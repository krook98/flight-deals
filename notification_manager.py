from twilio.rest import Client
import os
import smtplib

PHONE_NUMBER = os.environ.get('PHONE_NUMBER')
NOTIFICATION_NUMBER = os.environ.get('NOTIFICATION_NUMBER')
MY_EMAIL = os.environ.get('MY_EMAIL')
MY_PASSWORD = os.environ.get('MY_PASSWORD')


class NotificationManager:
    def __init__(self):
        self.account_sid = os.environ.get("account_sid")
        self.auth_token = os.environ.get("auth_token")
        self.client = Client(self.account_sid, self.auth_token)

    def send_message(self, message):
        message = self.client.messages.create(body=message, from_=NOTIFICATION_NUMBER, to=PHONE_NUMBER)

    def send_emails(self, emails, message, flight_link):
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(from_addr=MY_EMAIL,
                                    to_addrs=email,
                                    msg=f"Subject: Wykryto nizsza cene lotu!\n\n{message}\n"
                                        f"{flight_link}".encode('utf-8')
                                    )


