import datetime
# this class method creates a datetime object with the current date and time
now = datetime.datetime.today()
print(now.year)
print(now.hour)
print(now.minute)
print(now.weekday())
print(now.strftime("%a, %d %B %Y"))
long_ago = datetime.datetime(1999, 3, 14, 12, 30, 58)
print(long_ago) # remember that this calls str automatically
print(long_ago < now)
difference = now - long_ago
print(type(difference))
print(difference) # remember that this calls str automatically
