from datetime import date, time, datetime
today = date.today()
now = datetime.now()
print("Today's date is", today)
print("\nCurrent date and time are", now)
print("\nDate components are", today.year, today.month, today.day)