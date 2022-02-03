from twilio.rest import Client
import os

PHONE_NUMBER = os.environ.get('PHONE_NUMBER')
NOTIFICATION_NUMBER = os.environ.get('NOTIFICATION_NUMBER')


class NotificationManager:
    def __init__(self):
        self.account_sid = os.environ.get("account_sid")
        self.auth_token = os.environ.get("auth_token")
        self.client = Client(self.account_sid, self.auth_token)

    def send_message(self, message):
        message = self.client.messages.create(body=message, from_=NOTIFICATION_NUMBER, to=PHONE_NUMBER)
        print(message.sid)