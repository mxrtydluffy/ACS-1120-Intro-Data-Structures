import random
from histogram import histogram

def random_word(sentence):
    """
    Getting random word from the sentence
    """
    histogram_words = histogram(sentence)
    random_word = random.choices(
        list(histogram_words.keys()),
        weights = histogram_words.values(),
        k = 1
    )[0]

    return random_word

if __name__ == "__main__":
    sentence = "one fish two fish red fish blue fish"
    word_frequency = {}
    for _ in range(3000000):
        histogram_words = random_word(sentence)
        if random_word in word_frequency:
            word_frequency[random_word] += 1
        else:
            word_frequency[random_word] = 1
    for word in word_frequency:
        print(f"{word}: {word_frequency[word]}")