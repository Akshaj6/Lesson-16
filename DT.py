from datetime import datetime as DT
time = DT.now()
print("Hour =", time.hour)
print("Minute =", time.minute)
print("Second =", time.second)
print("Microsecond =", time.microsecond)
today = DT.today()
print(today.year)
print(today.month)
print(today.day)