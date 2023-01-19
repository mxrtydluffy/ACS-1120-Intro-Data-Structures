import random
import sys

# Browses for words in the words flie asnd return a random sentence with selected words.  
def generate_random_sentence(word_number):
    # sample pulls items from list
    with open("/usr/share/dict/words") as m:
        words = m.read().split()

    random_words = random.choices(words, k=word_number)
    return " ".join(random_words).capitalize() + "."

if __name__ == "__main__":
    number_of_words = int(sys.argv[1])
    print(generate_random_sentence(number_of_words))