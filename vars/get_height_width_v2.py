try:
    height = int(input("Enter height of rectangle: "))
    width = int(input("Enter width of rectangle: ")) 
    print("The area of the rectangle is %d " % (height * width))
except ValueError as e: # if a value error occurs, we will skip to this point
    print("Error reading height and width: %s" % e)
