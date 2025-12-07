import csv
import hashlib
import os

FOLDER = "files_to_monitor"
BASELINE = "baseline_hashes.csv"

def sha256_hash(path):
    hasher = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

#Load baseline hashes
baseline = {}
with open(BASELINE, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        baseline[row["filename"]] = row["sha256"]

current_files = os.listdir(FOLDER)

modified = []
deleted = []
new_files = []

#Detect modified and deleted
for filename, old_hash in baseline.items():
    filepath = os.path.join(FOLDER, filename)
    if os.path.exists(filepath):
        new_hash = sha256_hash(filepath)
        if new_hash != old_hash:
            modified.append(filename)
    else:
        deleted.append(filename)

#Detect new files
for filename in current_files:
    if filename not in baseline:
        new_files.append(filename)

print("Modified:", modified)
print("Deleted:", deleted)
print("New files:", new_files)
