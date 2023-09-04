# Write a program which uses a while loop to sum the squares of 
# integers (starting from 1) until the total exceeds 200. 
# Print the final total and the last number to be squared and added.
i = 1
sum = 0
while sum <= 200:
  sum = sum + i ** 2
  i = i + 1
print("The final total is %d" % sum)
