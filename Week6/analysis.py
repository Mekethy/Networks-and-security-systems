sample = r"'''"


import hashlib

def compute_hash(path, algorithm):
    h = hashlib.new(algorithm)
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()

print("MD5:    ", compute_hash(sample, "md5"))
print("SHA1:   ", compute_hash(sample, "sha1"))
print("SHA256: ", compute_hash(sample, "sha256"))

import re

def extract_strings(path):
    with open(path, "rb") as f:
        data = f.read()
    pattern = rb"[ -~]{4,}"       
    return re.findall(pattern, data)

strings = extract_strings(sample)
print("\nFirst 20 strings:")
for s in strings[:20]:
    print(s.decode(errors="ignore"))


import pefile

pe = pefile.PE(sample)

print("\nEntry Point:", hex(pe.OPTIONAL_HEADER.AddressOfEntryPoint))
print("Image Base:", hex(pe.OPTIONAL_HEADER.ImageBase))

print("\nImported DLLs and first 5 functions:")
for entry in pe.DIRECTORY_ENTRY_IMPORT:
    print(" ", entry.dll.decode())
    for imp in entry.imports[:5]:
        print("   -", imp.name.decode() if imp.name else "None")

import yara

rule_source = """
rule ContainsHTTP {
    strings:
        $s = "http"
    condition:
        $s
}
"""

rules = yara.compile(source=rule_source)
matches = rules.match(sample)

print("\nYARA matches:", matches)
