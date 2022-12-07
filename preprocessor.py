import csv
import json
import os


# path = input("Input file: ")
path = './Data/merged.json'
preprocessed = []

with open(path, 'r') as file:
    data = json.load(file)

    for key in data.keys():  # iterate over bibtex data
        entry = data[key]

        try:
            affiliation = entry['affiliations'].split(';')[0]  # get origin of the paper (leading)
            if not affiliation.__contains__('Germany'):  # skip if not german
                continue

            authors = entry['author']  # extract authors (with full names)
            if authors == '':  # skip if empty (in case Scopus did not have author data)
                continue
            first_author = authors.split(' and ')[0]  # extract leading author

            year = entry['year']  # get year
            if not year.isnumeric() or int(year) < 2000:
                continue

            try:
                citations = entry['note'].split(': ')[1].split(';')[0]  # get amount of citations
            except IndexError:
                citations = -1  # if not available -1
        except KeyError:
            continue

        preprocessed.append((first_author, year, citations))  # insert extracted data into the list


# write_path = input("Name output file: ")
write_path = './Data/preprocessed.csv'
print(f'Preprocessed data contains {len(preprocessed)} rows. Writing to "{write_path}"...')
with open(write_path, 'w', encoding="utf-8", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(preprocessed)

print("Finished.")