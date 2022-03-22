import random
import sys
sys.path.append("../src")
from settings import masking, deletion, insertion, seq_threshold, random_tokens

def word_corrupt(word: str, seq_length: int) -> str:
    percentage: float = random.uniform(0, 1)
    
    # If the sequence is likely a whole sentence (based on sequence length), don't corrupt the word
    if seq_length < seq_threshold:
        return word + " "
    
    # Perform corruptions
    if percentage < masking: # mask the original word
        return "<mask> "
    elif percentage < deletion: # delete the word
        return ""
    elif percentage < insertion: # insert a random token
        idx = random.randint(0, len(random_tokens) - 1)
        return f"{word} {random_tokens[idx]} "
    else:
        return word + " "
    