import random
import sys
sys.path.append("../src")
from settings import alphabets, punctuations

# Corrupt punctuation of the word
def punctuation_corruption(character: str, keep: float) -> str:
    if random.uniform(0, 1) <= keep:
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
        if i == len(word) - 2 and character in punctuations.values():
            #print("Punctuation modified")
            corrupted_word += punctuation_corruption(character, 0.6)
        elif random.uniform(0, 1) < character_percentage:
            idx: int = random.randint(0, len(alphabets) - 1)
            corrupted_word += alphabets[idx]
        else: 
            corrupted_word += character
    
    return corrupted_word