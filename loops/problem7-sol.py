months = ("January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October",
          "November", "December")

num_days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

month_dict = {}

for month, days in zip(months, num_days):
    month_dict[month] = days
print(month_dict.items())
month = input("Enter month:")
print("Number of days in " + month + " is " + str(month_dict[month]))
