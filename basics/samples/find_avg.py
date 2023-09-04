count = 0
total = 0
while True: 
  number = float(input("Enter a number:"))
  if (number == 0):
     break
  total = total + number
  count = count + 1
avg = total / count
print(f"The average is {avg}") 

