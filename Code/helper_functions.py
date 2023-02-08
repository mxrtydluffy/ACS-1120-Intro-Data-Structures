import re

def read_file(file_name):
    """
    Returns list of words from the corpus.txt file
    """
    with open(file_name) as r:
        words = re.findall(r"\b\w+(?[-']\w+)?\b", r.read().lower())
    return words