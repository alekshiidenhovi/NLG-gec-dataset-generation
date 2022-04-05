import pandas as pd
import random
import shutil
import os
from datasets import load_dataset
from datetime import datetime, date

from settings import training_amount, validation_amount, MAX_ARTICLES
from sentence_lists import create_sentence_lists

# Change the current working directory to src
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# Creates a tsv file with original and corrupted word sequences
def main():
    """Creates a tsv file with original and corrupted word sequences.
    Saves these files and used settings to the data file.
    
    Parameters
    ----------
    None
    
    Returns
    -------
    None"""
    wikipedia = load_dataset("wikipedia", "20200501.en")["train"]
    
    # Scramble indices
    random_indices = list(range(MAX_ARTICLES))
    random.shuffle(random_indices)
    
    # Create training and validation sentence lists
    train_orig_sequences, train_modified_sequences, end_idx = create_sentence_lists(wikipedia, 0, training_amount, random_indices)
    val_orig_sequences, val_modified_sequences, _ = create_sentence_lists(wikipedia, end_idx, validation_amount, random_indices)
    
    train_df = pd.DataFrame({"corrupted": train_modified_sequences, "original": train_orig_sequences})
    validation_df = pd.DataFrame({"corrupted": val_modified_sequences, "original": val_orig_sequences})
    
    # Write the dataframe to a tsv-file with the current time and amount of examples
    today = date.today()
    current_date = today.strftime("%b-%d-%Y") # MM-DD-YY
    
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S") # HH:MM:SS
    
    time = f"{current_date}_{current_time}"
    
    train_path = f"./data/training/wikipedia_{time}_{training_amount}.tsv"
    os.makedirs(os.path.dirname(train_path), exist_ok=True)
    train_df.to_csv(train_path, sep="\t", index=False, header=False)
    
    val_path = f"./data/validation/wikipedia_{time}_{validation_amount}.tsv"
    os.makedirs(os.path.dirname(val_path), exist_ok=True)
    validation_df.to_csv(val_path, sep="\t", index=False, header=False)
    
    # Copy current settings to the settings file
    settings_path = f"./data/settings/settings_{time}.py"
    os.makedirs(os.path.dirname(settings_path), exist_ok=True)
    shutil.copyfile("./settings.py", settings_path)
    

if __name__ == '__main__':
    main()