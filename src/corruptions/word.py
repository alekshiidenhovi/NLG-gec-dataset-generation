import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

import random
from settings import word_masking, word_deletion, word_insertion, seq_threshold, cum_word_distribution

def choose_word(chance: float) -> str:
    for cum_fraction, word in cum_word_distribution.items():
        if chance <= cum_fraction:
            return word
    
    return Exception("Error in the loop")

def word_corrupt(word: str, seq_length: int) -> str:
    percentage: float = random.uniform(0, 1)
    
    # If the sequence is likely a whole sentence (based on sequence length), don't corrupt the word
    if seq_length < seq_threshold:
        return word + " "
    
    # Perform corruptions
    if percentage < word_masking: # mask the original word
        return "<mask> "
    elif percentage < word_deletion: # delete the word
        return ""
    elif percentage < word_insertion: # insert a random token
        chance = random.uniform(0, 1)
        return f"{word} {choose_word(chance)} "
    else:
        return word + " "


if __name__ == '__main__':
    print(word_corrupt("Jason", 10))
    print(word_corrupt("Jason", 10))
    print(word_corrupt("Jason", 10))
    print(word_corrupt("Jason", 10))
    print(word_corrupt("Jason", 10))
    print(word_corrupt("Jason", 10))
    print(word_corrupt("Jason", 10))
    print(word_corrupt("Jason", 10))
    print(word_corrupt("Jason", 10))
    print(word_corrupt("Jason", 10))
    print(word_corrupt("Jason", 10))
    print(word_corrupt("Jason", 10))
    print(word_corrupt("Jason", 10))
    print(word_corrupt("Jason", 10))
    print(word_corrupt("Jason", 10))