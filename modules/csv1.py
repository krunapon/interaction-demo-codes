import csv
with open("names.csv") as f:
    rows = csv.reader(f)
    for row in rows:
        print(f"{row[0].strip()} studies {row[1].strip()} at {row[2].strip()}.")