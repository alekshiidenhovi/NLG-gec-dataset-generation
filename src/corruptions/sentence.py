import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from corruptions.word import word_corrupt
from corruptions.character import character_corrupt
from typing import List
import random

def sentence_corrupt(sentence: str, sentence_percentage: float) -> str:
    corrupted_sent: str = ""
        
    # If random number is lower than the corrupt_percentage, corrupt the word
    if random.uniform(0, 1) <= sentence_percentage:
        words: List[str] = sentence.split()
        for idx, orig_word in enumerate(words):
            sent_length: int = len(words)
            corrupted_word: str = character_corrupt(orig_word)
            
            if idx != sent_length - 1: # Corrupt all but the last word on word level
                corrupted_word = word_corrupt(corrupted_word, sent_length)
                
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