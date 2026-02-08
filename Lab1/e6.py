import datetime as dt

date = dt.datetime.__new__(dt.datetime,2026, 7, 1)
now = dt.datetime.now()
print(str(now.day)+"."+str(now.month)+"."+str(now.year), str(now.hour)+":"+str(now.minute)+":"+str(now.second))
print(date - now)