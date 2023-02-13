import random


class Dictogram(dict):
    """
    Need to display histogram and count displayed words
    """

    def __init__(self, word_list=None):
        super(Dictogram, self).__init__()
        self.types = 0
        self.tokens = 0
        if word_list is not None:
            for index, word in enumerate(word_list):
                self.add_count(word)
                if index + 1 <= len(word_list) - 1:
                    self.add_next(word, word_list[index + 1])
    
    def add_count(self, word, count=1):
        if word in self:
            self[word]["count"] += count
        else:
            self[word] = {"count": count, "next": {}}
            self.types += 1
        self.tokens += count

# entry_point = histogram.sample()

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
    return " ".join(sentence).captialize() + "."

print(build_map(source_text))