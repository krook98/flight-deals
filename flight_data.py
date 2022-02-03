import os

KIWI_ENDPOINT = 'tequila-api.kiwi.com/v2/search/'
KIWI_API_KEY = os.environ.get('KIWI_API_KEY')


class FlightData:
    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
