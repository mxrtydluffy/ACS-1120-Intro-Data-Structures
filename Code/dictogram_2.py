from markov_chain import Dictogram
from helper_functions import read_file

histogram_words = {}

def display_markov(source_text, number=1, order=1):
    
    histogram_words['filled'] = (
        Dictogram(source_text, order)
        if len(histogram_words) == 0
        else histogram_words['filled']
    )
    
    histogram = histogram_words['filled']
    tuple_list = []
    tuple_list.append(histogram.start_sample())

    # print(tuple_list)

    for _ in range(number):
        tuple_list.append(histogram.next_sample(tuple_list[-1]))
        while tuple_list[-1][-1][-1] not in [".", "!", "?"]:
            tuple_list.append(histogram.next_sample(tuple_list[-1]))
    list_of_words = []
    for index in range(len(tuple_list)):
        list_of_words.append(tuple_list[index][-1])
    return " ".join(list_of_words)

if __name__ == "__main__":
    text = read_file("./data/corpus.txt")
    print(display_markov(text, 5))