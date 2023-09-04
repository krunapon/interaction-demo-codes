import csv
with open("names.csv") as f:
    r = csv.reader(f)
    for row in r:
        print("{} studies {} at {}".
              format(row[0].strip(),
                     row[1].strip(),
                     row[2].strip()))
