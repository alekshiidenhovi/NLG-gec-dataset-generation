import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

import random
from typing import List
from settings import word_masking, word_deletion, word_insertion, cumu_word_distribution


def choose_word(chance: float) -> str:
    """Choose a random word from the distribution.
    
    Parameters
    ----------
    chance (float): Floating point number between 0 and 1 that determines which word is chosen
    
    Returns
    -------
    word (str): Random word from the distribution"""
    for cum_fraction, word in cumu_word_distribution.items():
        if chance <= cum_fraction:
            return word
    
    return Exception("Error in the loop")


def word_corrupt(words: List[str], idx: int) -> str:
    """Perform word level corruption on the word. Corruption methods include
    masking, deletion, insertion and swapping.
    
    Parameters
    ----------
    words (str): Words of the original sequence
    idx (str): Index of current word
    
    Returns
    -------
    corrupted_word (str): Original words or corrupted words
    idx (str): Index after corruption"""
    
    percentage: float = random.uniform(0, 1)
    first_word = words[idx]
    corrupted_word = ""
    
    # Perform corruptions
    if percentage < word_masking: # mask the original word
        corrupted_word = "<mask> "
    elif percentage < word_deletion: # delete the word
        corrupted_word = ""
    elif percentage < word_insertion: # insert a random token
        chance = random.uniform(0, 1)
        corrupted_word = f"{choose_word(chance)} {first_word} "
    elif idx + 1 < len(words): # swap words
        corrupted_word = f"{words[idx+1]} {first_word} "
        idx += 1
    else: # return the original word
        corrupted_word = f"{first_word} "
        
    return corrupted_word, idx + 1


if __name__ == '__main__':
    words = "I went to the river bank to enjoy the day.".split()
    print(word_corrupt(words, 0)[0])
    print(word_corrupt(words, 1)[0])
    print(word_corrupt(words, 2)[0])
    print(word_corrupt(words, 3)[0])
    print(word_corrupt(words, 4)[0])
    print(word_corrupt(words, 5)[0])
    print(word_corrupt(words, 6)[0])
    print(word_corrupt(words, 7)[0])
    print(word_corrupt(words, 8)[0])
    print(word_corrupt(words, 9)[0])
