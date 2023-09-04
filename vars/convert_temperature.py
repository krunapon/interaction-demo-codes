# this is a boolean value -- it can be either true or false.
correct_input = False

while not correct_input:  # this is a while loop
    try:
        t_f = float(input("Enter a temperature in Fahrenheit: "))
        t_c = (5 / 9) * (t_f - 32)
        print("Temperature %.2f in Fahrenheit is %.2f in Celsius" % (t_f, t_c))
    except ValueError:
        print("Please enter a valid floating point for the temperature.")
    else:  # this will be executed if there is no value error
        correct_input = True
