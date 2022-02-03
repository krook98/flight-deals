from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import sys
import traceback

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "WAW"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=180)

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    try:
        price = flight.price
    except AttributeError as err:
        exc_traceback = sys.exc_info()[2]
        print(f"No flights found.\n{err}\n{traceback.print_tb(exc_traceback)}")
    else:
        if flight.price < destination['lowestPrice (pln)']:
            notification_manager.send_message(
                message=f"Wykryto nizsza cene! Tylko {flight.price} PLN za lot z {flight.origin_city}-{flight.origin_airport} "
                        f"do {flight.destination_city}-{flight.destination_airport}, od {flight.out_date} do {flight.return_date}."
        )


