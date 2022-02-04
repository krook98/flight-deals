import os
import smtplib

MY_EMAIL = os.environ.get('MY_EMAIL')
MY_PASSWORD = os.environ.get('MY_PASSWORD')


class NotificationManager:
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


