# Regular expression module which is a collection 
# of pre-defined functions to process inoput text.
import re
from helper_functions import read_file

# Analyze frequency of words in a body of text
#find body of source text
sentence = "one fish two fish red fish blue fish"

def dictogram(source_text):
    """
    1.) Stored histogram in a dictionary.
    2.) Assigned list of words so the sentence can be split.
    3.) Looping in the sentence for the word to get each value.
    """
    histogram = {}
    list_of_words = read_file(source_text.lower())
    for word in list_of_words:
        histogram[word] = list_of_words.count(word)
    return histogram

def unique_words(histogram):
    """
    Returns the total count of unique words in the histogram argument
    and returns the total count of unique words in the histogram.
    1.) Need to get words in histogram and then update it.
    """
    return len(histogram)

def frequency(word, histogram):
    """
    Returns the number of times that words appears in a text.
    """
    if isinstance(histogram, dict):
        return histogram[word]
    elif isinstance(histogram, list):
        for x in range(len(histogram)):
            if word in histogram[x]:
                return histogram[x][1]

def listogram(source_text):
    """
    Returns histogram from a source text in terms of how many times it appears.
    """
    listogram = []
    list_of_words = re.finall(r"\w+", source_text.lower())
    helper_list = []
    for word in list_of_words:
        if word not in helper_list:
            listogram.append([word, list_of_words.count(word)])
            helper_list.append(word)
        return listogram

# Since have alot of files this is needed
if __name__ == "__main__":
    get_histogram = dictogram(sentence)
    my_listogram = listogram(sentence)
    print(get_histogram)
    print(unique_words(get_histogram))
    print(frequency('fish', get_histogram))