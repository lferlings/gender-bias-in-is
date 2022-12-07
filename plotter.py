import csv
import matplotlib.pyplot as plt


data = []
path = './Data/preprocessed.csv'

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

keys = list(occurance.keys())
keys.sort()
cumsum = {(keys[0] - 1): 0}
for key in keys:
    cumsum[key] = cumsum[key - 1] + occurance[key]


print(cumsum[2023] - cumsum[2000])
print(len(data))
print((cumsum[2023] - cumsum[2000])/len(data))

plt.bar(cumsum.keys(), cumsum.values())
plt.suptitle("Veröffentlichungen kumuliert seit 2000", fontsize=14)
plt.title("aus Deutschland in der Wirtschaftsinformatik", fontsize=11)
plt.show()
