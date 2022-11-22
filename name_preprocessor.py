female = {}
male = {}

# Read data
with open('./yob2021.txt', 'r') as file:
    line = file.readline().removesuffix('\n')
    while line != '':
        if line.startswith('#'):
            line = file.readline().removesuffix('\n')
            continue
        line = line.split(',')
        name = line[0]
        sex = line[1]
        occurrence = int(line[2])
        if sex == 'M':
            male[name] = occurrence
        else:
            female[name] = occurrence

        line = file.readline().removesuffix('\n')

unisex_set = set(male.keys()).intersection(set(female.keys()))

removals = 0
for name in unisex_set:
    males = male[name]
    females = female[name]

    threshold = 0.1
    if males/females < threshold:
        male.pop(name)
        removals = removals + 1
        print(f'Males/Females ratio for {name}: {males}/{females}={males/females}! Removed name from male.')
    elif females/males < threshold:
        female.pop(name)
        removals = removals + 1
        print(f'Females/Males ratio for {name}: {females}/{males}={females/males}! Removed name from female.')

print(removals, ' names has been removed.')

with open('./names.txt', 'w') as file:
    for name in female.keys():
        file.write(name + ',F\n')
    for name in male.keys():
        file.write(name + ',M\n')

