import csv
import matplotlib.pyplot as plt


data = []
path = '../Daten/preprocessed.csv'

with open(path, 'r', encoding="utf-8-sig") as file:
    reader = csv.reader(file)

    for row in reader:
        year = row[1]
        if year != '':
            data.append(int(year))

occurance = {}
for entry in data:
    amount = occurance.get(entry, 0)
    occurance[entry] = amount + 1


plt.bar(occurance.keys(), occurance.values())
plt.show()
