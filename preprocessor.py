import csv
import os


path = input("Input file: ")

if not os.path.isfile(path) or path.split('.').pop() != 'csv':
    print(f'{path} is not a valid file.')
    exit(-1)


preprocessed_data = []

with open(path, 'r', encoding="utf-8-sig") as file:
    data = csv.reader(file)

    for row in data:  # iterate over csv data
        authors = row[1]  # extract authors (with full names)
        if authors == '':  # skip if empty (in case Scopus did not have author data)
            continue

        first_author = authors.split(';')[0]  # extract leading author
        year = row[4]
        if year.isdecimal() and int(year) < 2000:
            continue
        preprocessed_data.append((first_author, year))  # insert extracted data into the list


write_path = input("Name output file: ")
print(f'Preprocessed data contains {len(preprocessed_data)} rows. Writing to "{write_path}"...')
with open(write_path, 'w', encoding="utf-8", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(preprocessed_data)

print("Finished.")