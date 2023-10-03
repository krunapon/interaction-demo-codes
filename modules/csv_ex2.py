import csv
MAX_GPA = 4.0
with open("gpas.csv", "w",newline='') as fw:
    w = csv.writer(fw)
    w.writerow([2.3, 3.4])
    w.writerow([3.2, 3.5])