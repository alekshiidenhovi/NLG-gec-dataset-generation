import os
import pandas as pd
import random
from datetime import datetime, date

from datasets import load_dataset
from sentence_lists import create_sentence_lists
from settings import MAX_ARTICLES


def create_sample_sentences(n_sentences: int):
    """Creates a tsv file with sample sentences and uploads it to the data file.
    
    Parameters
    ----------
    n_sentences (int): Amount of sample sentences
    
    Returns
    -------
    None"""
    
    wikipedia = load_dataset("wikipedia", "20200501.en")["train"]
    
    # Scramble indices
    random_indices = list(range(MAX_ARTICLES))
    random.shuffle(random_indices)
    
    # Create training and validation sentence lists
    orig_sequences, modified_sequences, idx = create_sentence_lists(wikipedia, 0, n_sentences, random_indices)
    
    df = pd.DataFrame({"original": orig_sequences})
    
    # Write the dataframe to a tsv-file with the current time and amount of examples
    today = date.today()
    current_date = today.strftime("%b-%d-%Y") # MM-DD-YY
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S") # HH:MM:SS
    time = f"{current_date}_{current_time}"
    
    path = f"./data/samples/wikipedia_{time}.tsv"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, sep="\t", index=False, header=False)


if __name__ == '__main__':
    create_sample_sentences(1000)