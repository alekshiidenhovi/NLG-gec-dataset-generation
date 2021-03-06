import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import re
from collections import Counter
from datasets import load_dataset
from utility import article_filter


def create_word_distribution(n_articles: int, n_words: int):
    """Creates a dictionary of random short word probabilities.
    
    Parameters
    ----------
    n_articles (int): number of articles
    n_words (int): amount of words in the created dictionary
    
    Returns
    -------
    prob_distribution (dict): dictionary with probabilities as keys and their corresponding words as values"""
    
    wikipedia = load_dataset("wikipedia", "20200501.en")["train"]
    word_distribution = Counter()
    regex = r'[^A-Za-z]([A-Za-z\-\']+)[^A-Za-z]'

    i = 0
    while i < n_articles:
        article = wikipedia[i]["text"]
        sequences = article_filter(article)
        for seq in sequences:
            words = re.findall(regex, seq)
            for word in words:
                if len(word) <= 5: # Filter words longer than 5 characters
                    word_distribution[word.lower()] += 1
                
        if i % 2500 == 0:
            print(f"Article no. {i+1}")
        i += 1

    prob_distribution = {}
    most_common_n_words = word_distribution.most_common(n_words)
    total_freq = sum(list(map(lambda pair: pair[1], most_common_n_words)))
    least_common_word = most_common_n_words[-1][0]
    cumulative_fraction = 0

    for word, freq in most_common_n_words:
        cumulative_fraction = round(cumulative_fraction + freq / total_freq, 6) if word != least_common_word else 1 # Return 1 for last character to prevent rounding errors
        prob_distribution[cumulative_fraction] = word

    return prob_distribution

if __name__ == '__main__':
    print(create_word_distribution(100000, 70))


