from datetime import date, time, datetime

today = date.today()
now = datetime.now()
print("todays date is", today)
print("\nCurrent date and time", now )

print("\nDate Components", today.day, today.month , today.year)