# Import set and csv modules
from builtins import set
import csv

import compare
from plot import plot_analysis
import hypothesis_testing


# Initialize empty sets for male and female names
male_set = set()
female_set = set()

# Open and read the first file containing names and genders
with open('data/names/names.txt', 'r', encoding="utf-8-sig") as file:
    # Read the first line of the file
    line = file.readline().removesuffix('\n')

    # Continue reading the file line by line until the end is reached
    while line != '':
        # Skip lines starting with '#', which are comments
        if line.startswith('#'):
            line = file.readline().removesuffix('\n')
            continue
        # Split the line into the name and gender, and add the name to the appropriate set
        name = line.split(',')[0]
        sex = line.split(',')[1]
        if sex == 'M':
            male_set.add(name.lower())
        else:
            female_set.add(name.lower())

        # Read the next line
        line = file.readline().removesuffix('\n')

# Open and read the second file containing names and genders
with open("data/names/wgnd_2_0_name-gender_nocode.csv", 'r', encoding="utf-8-sig") as file:
    # Create a CSV reader object
    reader = csv.reader(file)
    # Skip the first line, which is the header
    reader.__next__()
    # Iterate over the remaining lines in the file
    for row in reader:
        # Split the line into the name and gender, and add the name to the appropriate set
        name = row[0]
        sex = row[1]
        if sex == 'M':
            male_set.add(name)
        elif sex == 'F':
            female_set.add(name)

# Initialize a list to store the data from the third file
data = []
# Open and read the third file containing author names and other information
path = 'data/preprocessed.csv'
with open(path, 'r', encoding="utf-8") as file:
    # Create a CSV reader object
    reader = csv.reader(file)
    # Iterate over the lines in the file
    for row in reader:
        # Add the row to the data list
        data.append(row)

# Initialize counters for the number of male, female, and unclassified authors, and for the number of rows with no name provided
female = 0
male = 0
unclassified = 0
missing_name = 0

# Initialize a list to store the classified data
classified_data = []

# Iterate over the rows in the data
for row in data:
    try:
        # Extract the first name from the author name, handling multiple names and hyphenated names
        first_name = row[0].split(', ')[1].split(' ')[0]  # get first name

        # If the first name is followed by a period (e.g. "J. Thomas"), use the next name instead
        if first_name.endswith('.'):
            first_name = row[0].split(', ')[1].split(' ')[1]  # switch to "Thomas"

        # If the first name is hyphenated (e.g. "Jan-Thomas"), use the first part of the name
        first_name = first_name.split('-')[0]

        # Extract the year and citation count from the row
        year = row[1]
        citations = row[2]

        # Check if the first name is in the male or female set, and increment the appropriate counter
        if first_name.lower() in male_set:
            male = male + 1
            # Add the gender, year, and citation count to the classified data list
            classified_data.append(('M', year, citations))
        elif first_name.lower() in female_set:
            female = female + 1
            # Add the gender, year, and citation count to the classified data list
            classified_data.append(('F', year, citations))
        else:
            # If the gender could not be classified, increment the unclassified counter
            unclassified = unclassified + 1
    except IndexError:  # in case no first name is provided
        # If the author name is not in the expected format, increment the missing_name counter
        missing_name = missing_name + 1
        continue


# Print the total number of classified authors, and the number and percentage of male and female authors
print("Classified: ", male + female)
print(f"\tMale: {male}, {male * 100 / (male + female)}%")
print(f"\tFemale: {female}, {female * 100 / (male + female)}%")
# Print the number of unclassified authors and the number of rows with no name provided
print("Unclassified: ", unclassified)
print("No name provided: ", missing_name)


# Initialize dictionaries to store the number and citation count of male and female authors per year
males_per_year = {}
females_per_year = {}
male_citations_per_year = {}
female_citations_per_year = {}

# Iterate over the classified data
for publication in classified_data:
    # Extract the year and citation count
    year = int(publication[1])
    citations = int(publication[2])
    # Increment the appropriate counters in the dictionaries
    if publication[0] == 'M':
        males_per_year[year] = males_per_year.get(year, 0) + 1
        male_citations_per_year[year] = male_citations_per_year.get(year, 0) + max(0, citations)
    elif publication[0] == 'F':
        females_per_year[year] = females_per_year.get(year, 0) + 1
        female_citations_per_year[year] = female_citations_per_year.get(year, 0) + max(0, citations)


male_average_citations = {}
female_average_citations = {}

# Iterate over the keys (years) in the males_per_year dictionary
years = list(males_per_year.keys())
years.sort()
for year in years:
    # Calculate the average number of citations per publication for male and female authors in the current year
    male_average_citations[year] = male_citations_per_year[year] / males_per_year[year]
    female_average_citations[year] = female_citations_per_year[year] / females_per_year[year]


hypothesis_testing.test_h1(males_per_year.copy(), females_per_year.copy())
hypothesis_testing.test_h2(females_per_year.copy())
hypothesis_testing.test_h3(males_per_year.copy(), females_per_year.copy())
hypothesis_testing.test_h4(male_average_citations.copy(), female_average_citations.copy())

plot_analysis.plot_males_and_females(males_per_year.copy(), females_per_year.copy())
plot_analysis.plot_males_and_females_share(males_per_year.copy(), females_per_year.copy())
plot_analysis.plot_citations(male_average_citations.copy(), female_average_citations.copy())
plot_analysis.plot_sum(males_per_year, females_per_year)


male_share = {}
female_share = {}
for year in males_per_year.keys():
    all = males_per_year[year] + females_per_year[year]
    male_share[year] = males_per_year[year] * 100 / all
    female_share[year] = females_per_year[year] * 100 / all

compare.compare_institute(male_share, female_share)
compare.compare_students(male_share, female_share)
compare.compare_plots(male_share, female_share)

# path = './data/analyse/'
# with open(path + 'male_publications.csv', 'w') as file:
#     w = csv.writer(file)
#     for key in males_per_year.keys():
#         w.writerow((key, males_per_year[key]))
# with open(path + 'female_publications.csv', 'w') as file:
#     w = csv.writer(file)
#     for key in males_per_year.keys():
#         w.writerow((key, males_per_year[key]))
# with open(path + 'male_citations.csv', 'w') as file:
#     w = csv.writer(file)
#     for key in males_per_year.keys():
#         w.writerow((key, males_per_year[key]))
# with open(path + 'male_citations.csv', 'w') as file:
#     w = csv.writer(file)
#     for key in males_per_year.keys():
#         w.writerow((key, males_per_year[key]))

