months = ("January", "February", "March", "April", "May", "June", "July", "August", "September",
          "October", "November", "December")
days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30,31)
months_days = {}
i = 0
for month in months:
    months_days[month] = days[i]
    i = i + 1
print(months_days.items())
month = input("Enter month:")
print("Number of days in " + month + " is " + str(months_days[month]))
