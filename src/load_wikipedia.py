import pandas as pd
from datasets import load_dataset
from corruptions.sentence import sentence_corrupt
from settings import sentence_percentage
import re

def load_wikipedia():
    wikipedia = load_dataset("wikipedia", "20200501.en")["train"]
    
    orig_sequences = []
    modified_sequences = []

    include_articles = 1
    idx = 0
    while idx < include_articles:
        article = wikipedia[idx]
        
        text: str = article["text"] # Choose the text part of the article
        text = text.split("\n\nReferences")[0] # Remove reference section
        
        # Find all the individual chapters
        regex = r'\s?([^\n]+)'
        sequences = re.findall(regex, text) 
        
        for orig_seq in sequences:
            orig_seq = orig_seq.rstrip().lstrip()
            orig_sequences.append(orig_seq)
            modified_sequences.append(sentence_corrupt(orig_seq, sentence_percentage))
            
        idx += 1
        
    df = pd.DataFrame({"Original": orig_sequences, "Corrupted": modified_sequences})
    print(df)
    # text = text.split("\n\nReferences")[0]

    # sentences = re.findall(r'\s?([^\n]+)', text)
    # # print(sentences)
    # return sentences
load_wikipedia()