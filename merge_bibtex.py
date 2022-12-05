import os
import bibtexparser
import time
import json
import threading

jsons = []


def transform_to_json_string(bibtex_file_path):
    with open(bibtex_file_path, 'r', encoding="utf-8-sig") as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)

    bib = bib_database.get_entry_dict()
    jsons.append(json.dumps(bib))


dir = os.listdir("./BibTex Daten/Raw Data/")
threads = []

start = time.time()
for item in dir:
    path = "./BibTex Daten/Raw Data/" + item
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
print(time.time() - start, "ms elapsed.")

# add up json string
jsonStr = ""
for bib in jsons:
    jsonStr = jsonStr + bib

# write json to disk
with open("./BibTex Daten/merged.json", "w") as file:
    file.write(jsonStr)

print("Finished converting to json and saved.")
print(time.time() - start, "ms elapsed.")
