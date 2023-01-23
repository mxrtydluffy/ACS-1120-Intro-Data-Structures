# Analyze frequency of words in a body of text
#find body of source text
sentence = "one fish two fish red fish blue fish"

def histogram(source_text):
    """
    1.) Stored histogram in a dictionary.
    2.) Assigned list of words so the sentence can be split.
    3.) Looping in the sentence for the word to get each value.
    """
    histogram = {}
    list_of_words = source_text.split()
    for word in list_of_words:
        histogram[word] = list_of_words.count(word)
    return histogram

def unique_words(histogram):
    """
    Returns the total count of unique words in the histogram argument
    and returns the total count of unique words in the histogram.
    """

def freuency(word, histogram):
    """
    Returns the number of times tht words appears in a text.
    """

# Since have alot of files this is needed
if __name__ == "__main__":
    print(histogram(sentence))