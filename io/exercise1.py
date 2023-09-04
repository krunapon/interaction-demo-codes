filenames1 = (2, 10, 11, 3)
filenames2 = []
for t in filenames1:
    filename = "file_{:03d}".format(t)
    filenames2.append(filename)

print("{:30s} {:20s}".format("input filenames are", str(filenames1)))
print("{:30s} {:20s}".format("zero padded filenames", str(filenames2)))
filenames2.sort()
print("{:30s} {:20s}".format("sorted filenames are", str(filenames2)))
