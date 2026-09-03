import datetime
now = datetime.datetime.now()
#print(now)
print(now.date())
today = datetime.datetime.today()
print(today)
print(today.strftime("%H-%M-%S:%p"))

