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

    def add_next_word(self, word, following_word):
        if following_word in self[word]["next"]:
            self[word]["next"][following_word] += 1
        else:
            self[word]["next"][following_word] += 1

    def sample(self):
        dart = random.uniform(0, self.tokens)
        fence = 0
        for word in self:
            fence += self[word]["count"]
            if dart <= fence:
                return word

    def sample_next(self, word):
        following_words = self[word]["next"]

        following_histogram = {}
        following_tokens = 0

        for word in following_words:
            if word in following_histogram:
                following_histogram[word] += following_words[word]
            else:
                following_histogram[word] = following_words[word]
            following_tokens += following_words[word]

        dart = random.uniform(0, following_tokens)
        fence = 0
        for word in following_histogram:
            fence += following_histogram[word]
            if dart <= fence:
                return word

    def frequency(self, word):
        """
        Return frequency count of the displayed word.
        """
        return self[word]["count"] if word in self else 0
    
    def start_sample(self):
        start_histogram = {}
        start_tokens = 0
        for word in self:
            if word[-1] in ["!", "?", "."]:
                following_words = self[word]["next"]
                for next_word in following_words:
                    if next_word in start_histogram:
                        start_histogram[next_word] += following_words[next_word]
                    else:
                        start_histogram[next_word] = following_words[next_word]
                    start_tokens += following_words[next_word]
        dart = random.uniform(0, start_tokens)
        fence = 0
        for word in start_histogram:
            fence += start_histogram[word]
            if dart <= fence:
                return word

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