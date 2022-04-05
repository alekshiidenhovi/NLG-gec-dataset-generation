import random
from typing import List
from corruptions.sentence import sentence_corrupt
from settings import MAX_ARTICLES, MAX_SEQ_LENGTH, sentence_percentage
from utility import article_filter


def create_sentence_lists(dataset, start_idx: int, n_sentences: int, random_indices: List[int]):
    """Create filtered and corrupted sentence lists.
    
    Parameters
    ----------
    dataset (Dataset): Wikipedia dataset
    start_idx (int): Starting index for the first article
    n_sentences (int): Amount of sentences included to the list
    random_indices (List[int]): Randomised indices between [0, MAX_ARTICLES - 1]
    
    Returns
    -------
    orig_sequences (List[str]): List of filtered sentences
    modified_sequences (List[str]): List of corrupted sentences
    idx (int): Ending index"""
    
    orig_sequences: List[str] = []
    modified_sequences: List[str] = []
    
    n_articles: int = start_idx # Amount of articles looped through
    keep_looping: bool = True
    
    while keep_looping and n_articles < MAX_ARTICLES:
        random_idx: int = random_indices[n_articles] # Pick a randomized index from the list
        article: str = dataset[random_idx]["text"] # Dictionary with 'title' and 'text' keys
        sequences: List[str] = article_filter(article) # Get filtered sentences from the article
        
        for orig_seq in sequences:
            if len(orig_sequences) >= n_sentences:
                keep_looping = False
                break
            elif len(orig_seq.split()) < MAX_SEQ_LENGTH:
                orig_seq = orig_seq.rstrip().lstrip() # Remove extra whitespace from the start and end of the sequences
                orig_sequences.append(orig_seq)
                modified_sequences.append(sentence_corrupt(orig_seq, sentence_percentage))
        
        if n_articles % 1000 == 0:
            print(f"Filtered sentences: {len(orig_sequences)}")      
        n_articles += 1
        
    return orig_sequences, modified_sequences, n_articles