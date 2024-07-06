from datetime import timedelta
from datetime import datetime


def display_current_datetime():
    current_date = datetime.now()
    formatted_current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_current_date}")

    def calculate_future_date():
        number_of_days = int(
            input("Enter the number of days to add to the current date: ")
        )
        duration = timedelta(days=number_of_days)
        future_date = current_date + duration
        formatted_future_date = future_date.strftime("%Y-%m-%d %H:%M:%S")
        print(f"Future date: {formatted_future_date}")

    calculate_future_date()


display_current_datetime()
