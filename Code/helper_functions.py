import re

def read_file(file_name):
    """
    Returns list of words from the corpus.txt file
    """
    with open(file_name) as f:
        words = re.findall (r"\w+", f.read().lower())
    return words