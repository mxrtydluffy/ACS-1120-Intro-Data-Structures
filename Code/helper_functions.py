import re

def read_file(file_name):
    """
    Returns list of words from the corpus.txt file
    """
    with open(file_name) as m:
        words = re.findall(r"\b\w+(?[-']\w+)?\b", m.read().lower())
    return words