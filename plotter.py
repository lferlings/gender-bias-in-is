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

cumsum = {1953: 0}
keys = list(occurance.keys())
keys.sort()
for key in keys:
    cumsum[key] = cumsum[key - 1] + occurance[key]


print(cumsum[2023] - cumsum[2000])
print(len(data))
print((cumsum[2023] - cumsum[2000])/len(data))

plt.bar(cumsum.keys(), cumsum.values())
plt.show()
