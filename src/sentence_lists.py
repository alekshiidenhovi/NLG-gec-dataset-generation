import re

from datasets import load_dataset
from settings import MAX_SEQ_LENGTH, sentence_percentage
from corruptions.sentence import sentence_corrupt

def create_sentence_lists(dataset, start_idx: int, amount: int):
    orig_sequences = []
    modified_sequences = []
    idx = start_idx
    keep_looping = True
    
    while keep_looping:
        article = dataset[idx] # Dictionary with 'title' and 'text' keys
        
        text: str = article["text"] # Choose the text part of the article
        text = text.split("\n\nReferences")[0] # Remove reference section
        
        # Find all the individual chapters
        # regex = r'\s?([^\n]+)' # First version
        regex = r'([A-Z][^\t\n\.!?]*[\.!?])\s+'
        sequences = re.findall(regex, text) 
        sequences = list(filter(lambda seq: re.findall(r"\s[A-Za-z]{1,2}\.", seq) == [], sequences)) # Filter sentences that have been corrupted from words like Dr, Mr. etc
        sequences = list(filter(lambda seq: len(list(seq)) >= 10 and len(seq.split()) >= 3, sequences)) # Filter sequences that are less than 10 characters long or less than 3 words long
        
        for orig_seq in sequences:
            if len(orig_sequences) >= amount:
                keep_looping = False
                break
            elif len(orig_seq.split()) < MAX_SEQ_LENGTH:
                orig_seq = orig_seq.rstrip().lstrip() # Remove extra whitespace from the start and end of the sequences
                orig_sequences.append(orig_seq)
                modified_sequences.append(sentence_corrupt(orig_seq, sentence_percentage))
            
        idx += 1
        
    return orig_sequences, modified_sequences, idx