import random
import sys
  
def generate_random_sentence(word_number):
    """
    Browses for words in the words flie asnd return a random sentence with selected words.
    """
    with open("/usr/share/dict/words") as m:    # sample pulls items from list
        words = m.read().split()

    random_words = random.sample(words, k=word_number)
    return " ".join(random_words).capitalize() + "."

if __name__ == "__main__":
    number_of_words = int(sys.argv[1])
    print(generate_random_sentence(number_of_words))