import os
import re

FOLDER = "files_to_scan"

#Common suspicious signatures
SIGNATURES = [
    r"eval\(",
    r"base64\.b64decode",
    r"socket\.connect",
    r"exec\(",
    r"import os"
]
#Dictionary
suspicious = {}

#Scan files for suspicious signatures
for fname in os.listdir(FOLDER):
    path = os.path.join(FOLDER, fname)

    if not os.path.isfile(path):
        continue

    with open(path, "r", errors="ignore") as f:
        content = f.read()

    for sig in SIGNATURES:
        if re.search(sig, content):
            if fname not in suspicious:
                suspicious[fname] = []
            suspicious[fname].append(sig)


#Report suspicious files and signatures
for file, sigs in suspicious.items():
    print(f"{file} contains suspicious patterns: {sigs}")

# If no suspicious files or signatures found
if not suspicious:
    print("No suspicious signatures found.")
