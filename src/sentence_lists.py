from typing import List
from corruptions.sentence import sentence_corrupt
from settings import MAX_ARTICLES, MAX_SEQ_LENGTH, sentence_percentage
from utility import article_filter


def create_sentence_lists(dataset, start_idx: int, amount: int):
    """Create filtered and corrupted sentence lists.
    
    Parameters
    ----------
    dataset (Dataset): Wikipedia dataset
    start_idx (int): Starting index for the first article
    amount (int): Amount of articles included to the list
    
    Returns
    -------
    orig_sequences (List[str]): List of filtered sentences
    modified_sequences (List[str]): List of corrupted sentences
    idx (int): Ending index"""
    
    orig_sequences: List[str] = []
    modified_sequences: List[str] = []
    idx: int = start_idx
    keep_looping: bool = True
    
    while keep_looping and idx < MAX_ARTICLES:
        article: str = dataset[idx]["text"] # Dictionary with 'title' and 'text' keys
        sequences: List[str] = article_filter(article) # Get filtered sentences from the article
        
        for orig_seq in sequences:
            if len(orig_sequences) >= amount:
                keep_looping = False
                break
            elif len(orig_seq.split()) < MAX_SEQ_LENGTH:
                orig_seq = orig_seq.rstrip().lstrip() # Remove extra whitespace from the start and end of the sequences
                orig_sequences.append(orig_seq)
                modified_sequences.append(sentence_corrupt(orig_seq, sentence_percentage))
        
        if idx % 1000 == 0:
            print(f"Filtered sentences: {len(orig_sequences)}")      
        idx += 1
        
    return orig_sequences, modified_sequences, idx