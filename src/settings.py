# Main
MAX_SEQ_LENGTH = 40 # Maximum amount of words
MAX_ARTICLES = 6000000
training_amount = 200000 # Amount of training samples
validation_amount = 100 # Amount of validation samples


# Pattern corrupt
articles = ["a", "an", "the"]
article_percentage = 0.7


# Sentence corrupt
sentence_percentage = 0.7 # How many sentences get corrupted


# Word corrupt
word_percentage = 0.12 # Fraction of words corrupted
word_masking = 0.1 # Fraction of corruptions masked
word_deletion = 0.3 # ... deleted
word_insertion = 0.5 # ... inserted
word_swap = 0.65 # ... swapped
cum_word_distribution = {0.169499: 'the', 0.260296: 'and', 0.344015: 'of', 0.412124: 'in', 0.46743: 'to', 0.520268: 'a', 0.555566: 'was', 0.584494: 'is', 0.606845: 'as', 0.628624: 'for', 0.648958: 's', 0.66893: 'on', 0.688885: 'with', 0.706758: 'by', 0.721013: 'that', 0.734717: 'at', 0.747904: 'from', 0.760372: 'he', 0.772125: 'his', 0.783373: 'which', 0.792745: 'an', 0.801064: 'were', 0.809003: 'but', 0.816858: 'are', 0.824559: 'it', 0.831488: 'who', 0.838349: 'or', 0.844926: 'also', 0.851202: 'has', 0.857435: 'be', 0.863645: 'first', 0.869681: 'had', 0.875043: 'th', 0.880253: 'new', 0.885376: 'their', 0.890315: 'this', 0.895233: 'one', 0.899885: 'her', 0.904482: 'its', 0.909019: 'not', 0.913229: 'after', 0.917391: 'two', 0.921552: 'have', 0.925472: 'she', 0.929297: 'been', 0.933051: 'where', 0.936795: 'they', 0.940473: 'when', 0.943859: '-', 0.947113: 'into', 0.95032: 'may', 0.95352: 'other', 0.956621: 'time', 0.959701: 'years', 0.962658: 'all', 0.965432: 'such', 0.968143: 'more', 0.970788: 'then', 0.973388: 'would', 0.975987: 'only', 0.978578: 'born', 0.981149: 'while', 0.983636: 'over', 0.986105: 'up', 0.98848: 'city', 0.990829: 'there', 0.993154: 'made', 0.99544: 'most', 0.997723: 'used', 1: 'world'}


# Character corrupt
cum_char_distribution = {0.119367: 'e', 0.208253: 'a', 0.293737: 't', 0.369865: 'i', 0.44516: 'n', 0.517411: 'o', 0.583929: 'r', 0.6499: 's', 0.69744: 'h', 0.739351: 'l', 0.77934: 'd', 0.813247: 'c', 0.839561: 'u', 0.8654: 'm', 0.887827: 'f', 0.908348: 'p', 0.928105: 'g', 0.944788: 'w', 0.960851: 'b', 0.976036: 'y', 0.986446: 'v', 0.993327: 'k', 0.995676: 'j', 0.997553: 'x', 0.999013: 'z', 1: 'q'}
character_percentage = 0.005 # Fraction of characters corrupted
punctuations = { # The distribution of punctuation corruptions
  0.05: ";",
  0.10: ":",
  0.20: "",
  0.35: "!", 
  0.50: "?", 
  0.70: ",", 
  1: "."
}
char_insertion = 0.25
char_deletion = 0.5
char_replacement = 0.75
punct_percentage = 0.4 # How often punctuation gets corrupted
