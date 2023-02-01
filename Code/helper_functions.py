import re

def read_file(file_name):
    with open(file_name) as f:
        words = re.findall (r"\w+", f.read().lower())
    return words