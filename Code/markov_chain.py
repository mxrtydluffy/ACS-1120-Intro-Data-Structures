import random

class Dictogram(dict):
    """
    Need to display histogram and count displayed words
    """

    def __init__(self, list_of_words=None, order=1):
        super(Dictogram, self).__init__()
        self.types = 0
        self.tokens = 0
        self.order = order
        if list_of_words is not None:
            for index in range(len(list_of_words)):
                self.add_count(tuple(list_of_words[index: index + order]))
                if index + order <= len(list_of_words) - order:
                    self.add_next_word(tuple(list_of_words[index: index + order]), tuple(list_of_words[index+1: index + order + 1]))
    
    def add_count(self, word_tuple, count=1):
        if word_tuple in self:
            self[word_tuple]["count"] += count
        else:
            self[word_tuple] = {"count": count, "next": {}}
            self.types += 1
        self.tokens += count

    def add_next_word(self, word_tuple, following_tuple):
        if following_tuple in self[word_tuple]["next"]:
            self[word_tuple]["next"][following_tuple] += 1
        else:
            self[word_tuple]["next"][following_tuple] = 1

    def sample(self):
        dart = random.uniform(0, self.tokens)
        fence = 0
        for word_tuple in self:
            fence += self[word_tuple]["count"]
            if dart <= fence:
                return word_tuple

    def start_sample(self):
        start_histogram = {}
        start_tokens = 0
        for word_tuple in self:
            if word_tuple[-1][-1] in ["!", "?", "."]:
                following_tuples = self[word_tuple]["next"]
                for next_word in following_tuples:
                    if next_word in start_histogram:
                        start_histogram[next_word] += following_tuples[next_word]
                    else:
                        start_histogram[next_word] = following_tuples[next_word]
                    start_tokens += following_tuples[next_word]

        dart = random.uniform(0, start_tokens)
        fence = 0
        for word_tuple in start_histogram:
            fence += start_histogram[word_tuple]
            if dart <= fence:
                return word_tuple

    def next_sample(self, word_tuple):
        following_tuples = self[word_tuple]["next"]

        following_histogram = {}
        following_tokens = 0

        for word_tuple in following_tuples:
            if word_tuple in following_histogram:
                following_histogram[word_tuple] += following_tuples[word_tuple]
            else:
                following_histogram[word_tuple] = following_tuples[word_tuple]
            following_tokens += following_tuples[word_tuple]

        dart = random.uniform(0, following_tokens)
        fence = 0
        for word_tuple in following_histogram:
            fence += following_histogram[word_tuple]
            if dart <= fence:
                return word_tuple

    def frequency(self, word_tuple):
        """
        Return frequency count of the displayed word.
        """
        return self[word_tuple]["count"] if word_tuple in self else 0


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
        # Colored text indicators
        default = "\033[m"
        red = "\033[31m"
        yellow = "\033[33m"
        green = "\033[32m"
        # Searching for each word in histogram
        for word, count in histogram.items():
            observed_freq = count["count"] / histogram.tokens
            samples = hist_samples.frequency(word)
            sampled_freq = samples / hist_samples.tokens
            # Calculuing error between the observed & sampled
            error = (sampled_freq - observed_freq) / observed_freq
            colored_text = green if abs(error) < 0.05 else yellow if abs(error) < 0.1 else red
            print(
                "| {!r:<9} ".format(word)
                + "| {:>4} = {:>6.2%} ".format(count["count"], observed_freq)
                + "| {:>4} = {:>6.2%} ".format(samples, sampled_freq)
                + "| {}{:>+7.2%}{} |".format(colored_text, error, default)
            )
        print(divider)
        print()

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
    # Then tests the histograms on given letters of the word.
    # Finally test histogram on repeitive words
    import sys

    arg = sys.argv[1:]
    if len(arg) >= 1:
        print_histogram(arg)
    else:
        word = "appliedcomputerscience"
        print_histogram(list(word))
        # fish text
        fish_text = "one fish two fish red fish blue fish"
        print_histogram(fish_text.split())
        # Test histogram on words in a long repetitive sentence
        peterPiper_text = (
            "Peter Piper picked a peck of pickled peppers"
            "A peck of pickled peppers Peter Piper picked"
            "If Peter Piper picked a peck of pickled peppers"
            "Where's the peck of pickled peppers Peter Piper picked"
        )

        print_histogram(peterPiper_text.split())

if __name__ == "__main__":
    main()