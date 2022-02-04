from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager


ORIGIN_CITY_IATA = "WAW"
ADULTS = 2
CHILDREN = 0
INFANTS = 0

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_destination_data()

if sheet_data[0]["iataCode"] == "":
    city_names = [row["city"] for row in sheet_data]
    data_manager.city_codes = flight_search.get_destination_codes(city_names)
    data_manager.update_destination_codes()
    sheet_data = data_manager.get_destination_data()

destinations = {
    data["iataCode"]: {
        "id": data["id"],
        "city": data["city"],
        "price": data["lowestPrice"]
    } for data in sheet_data}

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=6 * 30)

for destination_code in destinations:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination_code,
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if flight is None:
        continue

    if flight.price < destinations[destination_code]["price"]:

        users = data_manager.get_customer_emails()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]

        message=f"Wykryto nizsza cene! Tylko {flight.price} PLN za lot z {flight.origin_city}-{flight.origin_airport} " \
                f"do {flight.destination_city}-{flight.destination_airport}, od {flight.out_date} do {flight.return_date}."

        if flight.stop_overs > 0:
            message += f"\nLot ma {flight.stop_overs} przesiadki w {flight.via_city}."

        link = f"www.kiwi.com/deep?affilid=jakubsokalskiflighttracker&currency=PLN&destination={flight.destination_airport}&lang=pl&origin={flight.origin_airport}" \
               f"&return=anytime&returnFromDifferentAirport=false&returnToDifferentAirport=false&adults={ADULTS}&children={CHILDREN}&infants={INFANTS}"
        notification_manager.send_emails(emails, message, link)

