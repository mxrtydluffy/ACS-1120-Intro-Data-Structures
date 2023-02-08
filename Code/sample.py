import random
from histogram import dictogram
from helper_functions import read_file

histogram_words = {}

def random_word(source_text):
    """
    Getting random word from the inital text
    then gets a random word from the histogram
    via frequency.
    """
    histogram_words["violence"] = (
        dictogram(source_text)
        if len(histogram_words) == 0
        else histogram_words["violence"]
    )
    random_word = random.choices(
        list(histogram_words["violence"].keys()),
        weights = histogram_words["violence"].values(),
        k=1,
    )[0]

    return random_word

def generate_sentence(source_text, number):
    """
    Generates random sentence from the text & word count #.
    """
    word_list = []
    for _ in range(number):
        word_list.append(random_word(source_text))
    return " ".join(word_list).capitalize() + "."

if __name__ == "__main__":
    word = read_file("./data/corpus.txt")
    word_frequency = {}
    for _ in range(12500):
        histogram_words = random_word(word)
        if random_word in word_frequency:
            word_frequency[random_word] += 1
        else:
            word_frequency[random_word] = 1
    for word in word_frequency:
        print(f"{word}: {word_frequency[word]}")