# This file is only for testing and overview, will be deleted later on
from builtins import set
import csv


female_set = set()
male_set = set()
with open('./names.txt', 'r') as file:
    line = file.readline().removesuffix('\n')
    while line != '':  # end of file
        if line.startswith('#'):  # comment lines
            line = file.readline().removesuffix('\n')
            continue
        name = line.split(',')[0]
        sex = line.split(',')[1]
        if sex == 'M':
            male_set.add(name)
        else:
            female_set.add(name)

        line = file.readline().removesuffix('\n')  # read next line

unisex_set = male_set.intersection(female_set)  # intersection of male and female is unisex
print('Resulting unisex names amount: ', len(unisex_set))
print('Resulting female names amount: ', len(female_set))
print('Resulting male names amount: ', len(male_set))


# Read author names
data = []
path = '../Daten/preprocessed.csv'
with open(path, 'r', encoding="utf-8-sig") as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)


female = 0
male = 0
unisex = 0
unclassified = 0
for row in data:
    try:
        first_name = row[0].split(',')[1].split(' ')[1]
        if first_name.endswith('.'):
            continue

        if first_name in unisex_set:
            unisex = unisex + 1
        elif first_name in male_set:
            male = male + 1
        elif first_name in female_set:
            female = female + 1
        else:
            # print(f'Could not classify {first_name}.')
            # print(row)
            unclassified = unclassified + 1
    except IndexError:  # in case no first name is provided
        print(row)
        continue

print("Male: ", male)
print("Female: ", female)
print("Unisex: ", unisex)
print("Unclassified: ", unclassified)
