import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 
# sys.path.insert(0,'..')

# import random
# from settings import character_percentage, cum_char_distribution, punctuations, punct_percentage

import random
from settings import character_percentage, cum_char_distribution, punctuations, punct_percentage

# Corrupt punctuation of the word
def punctuation_corruption(character: str, corrupt_punct: float) -> str:
    if random.uniform(0, 1) > corrupt_punct:
        return character
    else:
        punctuation_percentage: float = random.uniform(0, 1)
        for chance in punctuations.keys():
            if chance >= punctuation_percentage:
                return punctuations[chance]
        
        raise Exception("Error in the loop")

# Returns character based on the character distribution
def choose_character(chance: float) -> str:
    for cum_fraction, char in cum_char_distribution.items():
        if chance <= cum_fraction:
            return char
    
    return Exception("Error in the loop")

# Performs character level corruptions
def character_corrupt(word: str) -> str:
    corrupted_word: str = ""
    #print(word)
    
    for i, character in enumerate(word):
        #print(i, character)
        if i == len(word) - 1 and character in punctuations.values():
            #print("Punctuation modified")
            corrupted_word += punctuation_corruption(character, punct_percentage)
        elif random.uniform(0, 1) < character_percentage:
            chance: float = random.uniform(0, 1)
            corrupted_word += choose_character(chance)
        else: 
            corrupted_word += character
    
    return corrupted_word