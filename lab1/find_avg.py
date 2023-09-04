total = 0
count = 0
number = int(input("Enter a number: "))
while (number != 0):
  total = total + number
  count = count + 1
  number = int(input("Enter a number: "))
if (count == 0):
  avg = 0
else:
  avg = total / count
print(avg)

