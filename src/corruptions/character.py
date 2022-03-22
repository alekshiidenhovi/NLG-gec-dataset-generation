import sys
sys.path.insert(0,'..')

import random
from settings import alphabets, punctuations, punct_percentage

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

def character_corrupt(word: str) -> str:
    character_percentage: float = 0.005
    corrupted_word: str = ""
    #print(word)
    
    for i, character in enumerate(word):
        #print(i, character)
        if i == len(word) - 1 and character in punctuations.values():
            #print("Punctuation modified")
            corrupted_word += punctuation_corruption(character, punct_percentage)
        elif random.uniform(0, 1) < character_percentage:
            idx: int = random.randint(0, len(alphabets) - 1)
            corrupted_word += alphabets[idx]
        else: 
            corrupted_word += character
    
    return corrupted_word