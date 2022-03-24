import pandas as pd
import re
import shutil
import os
from datasets import load_dataset
from datetime import datetime, date

from corruptions.sentence import sentence_corrupt
from settings import sentence_percentage, include_articles, MAX_SEQ_LENGTH


# Change the current working directory to src
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# Creates a tsv file with original and corrupted word sequences
def main():
    wikipedia = load_dataset("wikipedia", "20200501.en")["train"]
    
    orig_sequences = []
    modified_sequences = []

    idx = 0
    while idx < include_articles:
        article = wikipedia[idx] # Dictionary with 'title' and 'text' keys
        
        text: str = article["text"] # Choose the text part of the article
        text = text.split("\n\nReferences")[0] # Remove reference section
        
        # Find all the individual chapters
        regex = r'\s?([^\n]+)'
        sequences = re.findall(regex, text) 
        
        for orig_seq in sequences:
            if len(orig_seq.split()) < MAX_SEQ_LENGTH:
                orig_seq = orig_seq.rstrip().lstrip() # Remove extra whitespace from the start and end of the sequences
                orig_sequences.append([orig_seq])
                modified_sequences.append(sentence_corrupt(orig_seq, sentence_percentage))
            
        idx += 1
        
    df = pd.DataFrame({"corrections": orig_sequences, "sentence": modified_sequences})
    
    # Write the dataframe to a tsv-file with the current time and amount of examples
    today = date.today()
    current_date = today.strftime("%b-%d-%Y") # MM-DD-YY
    
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S") # HH:MM:SS
    
    setup = f"{current_date}_{current_time}_{include_articles}"
    
    file_name = f"../data/datasets/wikipedia_{setup}.tsv"
    df.to_csv(file_name, sep="\t")
    
    # Copy current settings to the settings file
    shutil.copyfile("./settings.py", f"../data/settings/settings_{setup}.py")
    

if __name__ == '__main__':
    main()