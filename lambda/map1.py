celsius = [39.2, 36.5, 37.3]
print(celsius)
fahrenheit = map(lambda x: (float(9)/5) * x + 32, celsius)
print(list(fahrenheit))
