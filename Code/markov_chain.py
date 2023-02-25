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

    def next_sample(self, word):
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


    #######################
    #   Print functions   #
    #######################

    def print_samples(histogram):
        """
        Prints histogram samples & calculates observed and sampled frequency
        """
        print("Histogram Samples:")
        list_of_samples = [histogram.sample() for _ in range(10000)]
        hist_samples = Dictogram(list_of_samples)
        print("samples: {}".format(hist_samples))
        print()
        print("Instance frequeny and error from the distinguished frquency:")
        header = "| Word Type | Observered Frequency | Sampled Frequency | Error |"
        divider = "-" * len(header)
        # Making samples appear
        print(divider)
        print(header)
        print(divider)
        for word, count in histogram.items():
            observed_freq = count["count"] / histogram.tokens
            samples = hist_samples.frequency(word)
            sampled_freq = samples / hist_samples.tokens
            # Calculuing error between the observed & sampled
            error = (sampled_freq - observed_freq) / observed_freq

            # define colors later

    def print_histogram(list_of_words):
        print()
        print('''
        Histogram:
        Word list: {}'''.format(list_of_words))
        histogram = Dictogram(list_of_words)
        print("Dictogram: {}".format(histogram))
        print("{} tokens, {} types".format(histogram.tokens, histogram.types))
        for word in list_of_words[-2:]:
            freq = histogram.frequency(word)
            print("{!r} occurs {} times".format(word, freq))
        print()
        print_samples(histogram)

    

    #######################
    #    Main function    #
    #######################

def main():
    import sys
    # Provides info about constants functions etc.
    import sys

    arg = sys.argv[1:]
    if len(arg) >= 1:
        