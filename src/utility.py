import re
from pattern.en import tag
from typing import List


def contains_verb(seq: str):
    """Checks for verbs in the sequence. Returns true if there is at least one verb
    and false if there are no verbs in the sequence
    
    NOTE: POS-tags from https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
    
    Parameters
    ----------
    seq (str): Word sequence under investigation
    
    Returns
    -------
    contains_verb (bool): True if sequence contains at least one verb, false otherwise"""
    
    for word, pos in tag(seq):
        if pos.startswith("VB"):
            return True
    
    return False


def remove_parantheses(sentence: str):
    """Removes obsolete parantheses from a sentence.
    
    Parameters
    ----------
    sentence (str): Sentence to be filtered
    
    Returns
    -------
    filtered_sentence (str): Sentence with extra parantheses removed"""
    
    split_sentence = sentence.split(" () ") # Split sentence on the extra parantheses.
    return " ".join(split_sentence)


def article_filter(text: str):
    """Performs regex extraction and filtering of the sentences.
    
    Parameters
    ----------
    text (str): Unfiltered Wikipedia article

    Returns
    -------
    sequences (List[str]): List of filtered sentences"""
    
    text = text.split("\n\nReferences")[0] # Remove reference section
        
    # Find all the individual chapters
    regex = r'([A-Z][^\t\n\.!?]*[\.!?])\s+'
    sequences: List[str] = re.findall(regex, text) 
    sequences = list(filter(lambda seq: re.findall(r"\s[A-Za-z]{1,2}\.", seq) == [], sequences)) # Filter sentences that have been corrupted from words like Dr, Mr. etc
    sequences = list(filter(lambda seq: len(list(seq)) >= 10 and len(seq.split()) >= 3, sequences)) # Filter sequences that are less than 10 characters long or less than 3 words long
    sequences = list(filter(lambda seq: contains_verb(seq), sequences)) # Filter sequences that don't contain any verbs
    sequences = list(map(lambda seq: remove_parantheses(seq), sequences))
    
    return sequences