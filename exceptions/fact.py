def fact(x):
   f = 1
   for i in range(1,x+1):
      print (i)
      f = f * i
   return f
if __name__=="__main__":
   print ("factorial of 5=",fact(5))
