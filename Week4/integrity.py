import hashlib
import os
import csv
from datetime import datetime

FOLDER = "files_to_monitor"
OUTPUT = "baseline_hashes.csv"

#Function to compute SHA256 hash of a file

def sha256_hash(path):
    hasher = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

rows = []

#Loop through files in folder
for filename in os.listdir(FOLDER):
    filepath = os.path.join(FOLDER, filename)
    if os.path.isfile(filepath):
        file_hash = sha256_hash(filepath)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        rows.append([filename, file_hash, timestamp])


#Write hashes to CSV
with open(OUTPUT, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["filename", "sha256", "timestamp"])
    writer.writerows(rows)

print("Baseline hashes saved.")
