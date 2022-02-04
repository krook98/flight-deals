import os
import requests


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=os.environ.get('SHEETY_URL'))
        result = response.json()
        self.destination_data = result['prices']
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{os.environ.get('SHEETY_URL')}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_customer_emails(self):
        response = requests.get(url=os.environ.get('SHEETY_USERS'))
        data = response.json()
        self.customer_data = data['users']
        return self.customer_data

