import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

import random
from settings import character_percentage, cum_char_distribution, punctuations, punct_percentage, char_insertion, char_deletion, char_replacement

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
def choose_character() -> str:
    for cum_fraction, char in cum_char_distribution.items():
        if random.uniform(0, 1) <= cum_fraction:
            return char
    
    return Exception("Error in the loop")

# Performs character level corruptions: insertion, deletion, replacement and swap
def character_corrupt(word: str) -> str:
    corrupted_word: str = ""
    
    i = 0 
    while i < len(word):
        character = word[i]
        if i == len(word) - 1 and character in punctuations.values(): # Perform punctuation corruption
            corrupted_word += punctuation_corruption(character, punct_percentage)
        elif random.uniform(0, 1) < character_percentage: # Perform character level corruption
            corruption = ""
            chance = random.uniform(0, 1)
            
            if chance < char_insertion: # Insert a random character
                corruption = character + choose_character()
            elif chance < char_deletion: # Delete the original character
                corruption = ""
            elif chance < char_replacement: # Replace the original character with a random character
                corruption = choose_character()
            elif i != len(word) - 1: # Swap characters if not the last word in sentence
                corruption = word[i+1] + character
                i += 1
            else:
                corruption = character
                
            corrupted_word += corruption
        else: # No character level corruption
            corrupted_word += character
            
        i += 1
    
    return corrupted_word