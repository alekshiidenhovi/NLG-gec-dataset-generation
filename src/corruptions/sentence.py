import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from corruptions.word import word_corrupt
from corruptions.character import character_corrupt
from typing import List
from settings import word_percentage
import random

def sentence_corrupt(sentence: str, sentence_percentage: float) -> str:
    """Perform sentence level corruption. First perform character level corruption and
    then word level corruption.
    
    Parameters
    ----------
    sentence (str): sentence to be corrupted
    sentence_percentage (float): percentage of sentences to be corrupted
    
    Returns
    -------
    corrupted_sent (str): corrupted sentence"""
    
    corrupted_sent: str = ""
        
    # If random number is lower than the corrupt_percentage, corrupt the word
    if random.uniform(0, 1) <= sentence_percentage:
        words: List[str] = sentence.split()
        idx = 0
        while idx < len(words):
            corrupted_word = words[idx] + " "
            if random.uniform(0, 1) <= word_percentage:
                corrupted_word, idx = word_corrupt(words, idx)
            else:
                idx += 1
            corrupted_word = character_corrupt(corrupted_word)
            corrupted_sent += corrupted_word
    else:
        corrupted_sent = sentence
            
    return corrupted_sent.rstrip().lstrip()


if __name__ == '__main__':
    sentence = "A transformer is a deep learning model that adopts the mechanism of self-attention, differentially weighting the significance of each part of the input data."

    print(sentence_corrupt(sentence, 1))
    print(sentence_corrupt(sentence, 1))
    print(sentence_corrupt(sentence, 1))
    print(sentence_corrupt(sentence, 1))
    print(sentence_corrupt(sentence, 1))