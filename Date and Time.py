import datetime

date = datetime.date(2026, 10, 2)
today = datetime.date.today()

time = datetime.time(12, 30, 2)
now = datetime.datetime.now()

now = now.strftime("%H:%M:%S %m-%d-%Y")

target_datetime = datetime.datetime(2026, 1, 2, 12, 30, 2)
current_date = datetime.datetime.now()

if target_datetime < current_date:
    print("Target date is before current date")
else:
    print("Target date is after current date")