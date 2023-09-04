import csv
with open('pets.csv', 'w') as f:
    w = csv.writer(f)
    w.writerow(['Fluffy', 'cat'])
    w.writerow(['Max', 'dog'])
