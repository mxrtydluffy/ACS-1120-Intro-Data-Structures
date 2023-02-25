from markov_chain import Dictogram
from helper_functions import read_file

def display_markov(source_text, number =1):
    histogram = Dictogram(source_text)
    list_of_words = []
    list_of_words.append(histogram.start_sample())
    for _ in range(number):
        list_of_words.append(histogram.next_sample(list_of_words[-1]))
        while list_of_words[-1][-1] not in ["?", ".", "!"]:
            list_of_words.append(histogram.next_sample(list_of_words[-1]))
        return " ".join(list_of_words)

if __name__ == "__main__":
    text = read_file("./data/corpus.txt")
    print(display_markov(text, 10))