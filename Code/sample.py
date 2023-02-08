import random
from histogram import dictogram

def random_word(source_text):
    """
    Getting random word from the sentence
    """
    histogram_words = dictogram(sentence)
    random_word = random.choices(
        list(histogram_words.keys()),
        weights = histogram_words.values(),
        k = 1
    )[0]

    return random_word

def generate_sentence(source_text, number):
    word_list = []
    for _ in range(number):
        word_list.append(random_word(source_text))
    return " ".join(word_list).capitalize() + "."

if __name__ == "__main__":
    sentence = "./data/corpus.txt"
    word_frequency = {}
    for _ in range(3000000):
        histogram_words = random_word(sentence)
        if random_word in word_frequency:
            word_frequency[random_word] += 1
        else:
            word_frequency[random_word] = 1
    for word in word_frequency:
        print(f"{word}: {word_frequency[word]}")