import os
import bibtexparser
import time
import json
import threading

jsons = []
database = {}


def transform_to_json_string(bibtex_file_path):
    with open(bibtex_file_path, 'r', encoding="utf-8-sig") as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)

    bib = bib_database.get_entry_dict()
    print(f"{bibtex_file_path} contains {len(bib)} entries.")
    for key in bib.keys():
        database[key] = bib[key]
    print(bibtex_file_path, " finished.")


dir = os.listdir("data/raw_data/")
threads = []

start = time.time()
for item in dir:
    path = "./data/raw_data/" + item
    if os.path.isfile(path):  # for file in dir
        threads.append(threading.Thread(target=transform_to_json_string, args=(path,)))

    else:  # read sub dir
        for subdir_file in os.listdir(path):
            threads.append(threading.Thread(target=transform_to_json_string, args=(path + '/' + subdir_file,)))

print("Starting threads...")
# start all threads
for t in threads:
    t.start()

# wait for all threads to finish
for t in threads:
    t.join()
print((time.time() - start)/60, "m elapsed.")

start = time.time()
# add up json string
jsonStr = json.dumps(database)

# write json to disk
with open("data/merged.json", "w") as file:
    file.write(jsonStr)

print("Finished converting to json and saved.")
print(time.time() - start, "s elapsed.")
