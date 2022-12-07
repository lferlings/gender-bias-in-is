import csv
import os

path = './Institute Data/'
file_names = os.listdir(path)

data = {}

for name in file_names:  # iterate over dir contents
    with open(path + name, 'r') as file:
        csv_reader = csv.reader(file, delimiter=';')

        # accumulate data
        for row in csv_reader:
            year = row[0]
            male = data.get(year, (0, 0))[0] + int(row[1])
            female = data.get(year, (0, 0))[1] + int(row[2])
            data[year] = (male, female)

with open('institute_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    keys = list(data.keys())
    keys.sort()
    for year in keys:
        male = data[year][0]
        female = data[year][1]
        row = (year, male + female, male, female)
        print(row, f", Male: {male/(male + female) * 100}%, Female: {female/(male + female) * 100}")
        writer.writerow(row)
