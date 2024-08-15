from datetime import date
day_now = date.today()
print(day_now)

xday = date(1980,1,1)
td = day_now - xday
print(td)
