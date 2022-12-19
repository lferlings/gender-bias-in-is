import csv
import matplotlib.pyplot as plt


data = []
path = 'data/preprocessed.csv'

with open(path, 'r', encoding="utf-8-sig") as file:
    reader = csv.reader(file)

    for row in reader:
        year = row[1]
        if year != '':
            data.append(int(year))

occurrence = {}
for entry in data:
    amount = occurrence.get(entry, 0)
    occurrence[entry] = amount + 1

keys = list(occurrence.keys())
keys.sort()
cumsum = {}
for key in keys:
    cumsum[key] = cumsum.get(key - 1, 0) + occurrence[key]


print(cumsum[2023] - cumsum[2000])
print(len(data))
print((cumsum[2023] - cumsum[2000])/len(data))

plt.bar(cumsum.keys(), cumsum.values())
plt.suptitle("Veröffentlichungen kumuliert seit 2000", fontsize=14)
plt.title("aus Deutschland in der Wirtschaftsinformatik", fontsize=11)
plt.show()
