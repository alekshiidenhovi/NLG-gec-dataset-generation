from collections import Counter
from datasets import load_dataset
import re


def create_char_distribution(n_articles: int):
    """Creates a dictionary of the alphabet probabilities.
    
    Parameters
    ----------
    n_articles (int): number of articles
    
    Returns
    prob_distribution (dict): dictionary with probabilities as keys and corresponding alphabets as values"""
    
    wikipedia = load_dataset("wikipedia", "20200501.en")["train"]
    
    char_distribution = Counter()
    regex = r'([A-Za-z])'

    i = 0
    while i < n_articles:
        article = wikipedia[i]["text"]
        characters = re.findall(regex, article)
        for char in characters:
            char_distribution[char.lower()] += 1
        i += 1

    prob_distribution = {}
    total_freq = sum([freq for freq in char_distribution.values()])
    least_common_char = char_distribution.most_common()[-1][0]
    cumulative_fraction = 0

    for char, freq in char_distribution.most_common():
        cumulative_fraction = round(cumulative_fraction + freq / total_freq, 6) if char != least_common_char else 1 # Return 1 for last character to prevent rounding errors
        prob_distribution[cumulative_fraction] = char
    
    return prob_distribution

if __name__ == '__main__':
    print(create_char_distribution(100000))


