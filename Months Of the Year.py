import datetime
months = []
for month_number in range(1,13):
    date = datetime.datetime(2025, month_number, 1)
    month_name = date.strftime("%B")
    months.append(month_name)
print("The months of the year are :", months)