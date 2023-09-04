total = 0
count = 0
while (True):
    num = int(input("Enter an integer: "))
    if num < 0:
        break
    total = total + num
    count = count + 1
if count == 0:
    print("You haven't entered a positive number")
else:
    print("Average is ", total/count)
