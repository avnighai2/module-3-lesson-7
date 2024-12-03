import random
from datetime import timedelta, datetime

def generateRandomDates(start_date, end_date, k):
    random_dates = []
    date_range = end_date = start_date
    for i in range(k):
        random_days = random.randint(0, date_range.day)
        random_date = start_date + timedelta( days = random_days)
        random_dates.append(random_date)
    return random_dates
start_date = datetime(2024, 12, 3)
end_date = datetime(2024, 12, 25)
random_dates = generateRandomDates(start_date, end_date, 5)
print("The random dates generated are:")
for index, date in enumerate(random_dates):
    print(f"{index+1}.{date.strftime('%Y - %m - %d')}")