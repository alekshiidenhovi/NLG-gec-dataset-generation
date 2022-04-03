import pandas as pd
import shutil
import os
from datasets import load_dataset
from datetime import datetime, date

from corruptions.sentence import sentence_corrupt
from settings import training_amount, validation_amount, sentence_percentage, MAX_SEQ_LENGTH
from sentence_lists import create_sentence_lists

# Change the current working directory to src
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# Creates a tsv file with original and corrupted word sequences
def main():
    wikipedia = load_dataset("wikipedia", "20200501.en")["train"]
    
    # Create training and validation sentence lists
    train_orig_sequences, train_modified_sequences, end_idx = create_sentence_lists(wikipedia, 0, training_amount)
    val_orig_sequences, val_modified_sequences, _ = create_sentence_lists(wikipedia, end_idx, validation_amount)
    
    train_df = pd.DataFrame({"corrupted": train_modified_sequences, "original": train_orig_sequences})
    validation_df = pd.DataFrame({"corrupted": val_modified_sequences, "original": val_orig_sequences})
    
    # Write the dataframe to a tsv-file with the current time and amount of examples
    today = date.today()
    current_date = today.strftime("%b-%d-%Y") # MM-DD-YY
    
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S") # HH:MM:SS
    
    time = f"{current_date}_{current_time}"
    
    train_path = f"./data/training/wikipedia_{time}_{training_amount}.tsv"
    train_df.to_csv(train_path, sep="\t", index=False, header=False)
    
    val_path = f"./data/validation/wikipedia_{time}_{validation_amount}.tsv"
    validation_df.to_csv(val_path, sep="\t", index=False, header=False)
    
    # Copy current settings to the settings file
    shutil.copyfile("./settings.py", f"./data/settings/settings_{time}.py")
    

if __name__ == '__main__':
    main()