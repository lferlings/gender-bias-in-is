import csv
import os

path = input("Choose directory: ")

merged_csv = []

for item in os.listdir(path):
    if os.path.isfile(path + item):
        with open(path + item, 'r', encoding="utf-8-sig") as file:
            data = csv.reader(file)
            length = 0
            first = data.__next__()

            # Ensure headline/titles are excluded
            if first[0] != 'Authors' and first[1] != 'Author full names':  # ...
                merged_csv.append(first)  # if first is not title row, append
                length = length + 1

            for row in data:
                length = length + 1
                merged_csv.append(row)
            print(f"Read {length} entries from {item}.")


write_path = input("Name output file: ")
print(f'Merged CSV contains {len(merged_csv)} rows. Writing to "{write_path}"...')

with open(write_path, 'w', encoding="utf-8", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(merged_csv)

print("Finished.")

if __name__ == '__main__':
    pass
