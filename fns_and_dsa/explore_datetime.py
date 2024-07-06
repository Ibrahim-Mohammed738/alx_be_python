from datetime import timedelta
from datetime import datetime


def display_current_datetime():
    current_date = datetime.today()
    print(f"Current date and time:{current_date}")


def calculate_future_date():
    number_of_days = int(
        input(f"Enter the number of days to add to the current date: ")
    )
    duration = timedelta(days=number_of_days)
    future_date = current_date + duration
    print(f"Future date: {future_date}")


calculate_future_date()


display_current_datetime()
