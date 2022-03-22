from corruptions.sentence import sentence_corrupt
from typing import List, NamedTuple

def main(filename: str, sentence_percentage: float):
    # Download the uncorrupted sentences from a file
    with open(filename, 'r') as f:
        sentences: List[str] = f.read()
    
    sentence_pairs: List[NamedTuple[str, str]] = []
    
    # Loop over uncorrupted sentences
    for orig_sentence in sentences:
        corrupted_sent = sentence_corrupt(orig_sentence, sentence_percentage)
                
        sentence_pairs.append((orig_sentence, corrupted_sent))

    # Read the sentence pairs to a tsv-file


if __name__ == '__main__':
    main()