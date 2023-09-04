weight = 400
print("weight is %d" % weight)
if weight <= 1000:
    if weight <= 300:
        cost = 5
    else:
        cost = 5 + 2 * round((weight - 300)/100)
    print("Your parcel will cost R%d." % cost)
else:
    print("Maximum weight for small parcel exceeded.")
    print("Use large parcel service instead.")
