from dictogram import Dictogram
from histogram import file_reader
import random

source_text = file_reader("./data/corpus.txt")
histogram = Dictogram(source_text)

entry_point = histogram.sample()

def build_map(source_text):
    words = source_text
    histogram = {}
    for i in range(len(words) -1):
        word = words[i]
        following_word = words[i + 1]
        if word in histogram:
            histogram[word].append(following_word)
        else:
            histogram[word] = (following_word)
    return histogram

def sample_model(histogram, word):
    following_words = histogram[word]
    return random.choice(following_words)

def make_sentence(histogram, first_word):
    sentence = [first_word]
    word = first_word
    while word in histogram:
        next_word = sample_model(histogram, word)
        sentence.append(next_word)
        word = next_word
    return " ".join(sentence)

print(build_map(source_text))