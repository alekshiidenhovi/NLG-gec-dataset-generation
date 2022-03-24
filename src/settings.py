# Main
include_articles = 100000 # How many articles are included to the dataset, one article contains ~20 word sequences

# Sentence corrupt
sentence_percentage = 0.7 # How many sentences get corrupted

# Word corrupt
masking = 0.04 # Fraction of words masked
deletion = 0.08 # ... deleted
insertion = 0.10 # ... inserted
seq_threshold = 8 # Sequence length threshold for word corruptions
random_tokens = ["a", "an", "the", "on", "in", "out", "at", "to", "from", # Random tokens to be inserted
                "of", "off", "for", "with", "as", "and", "but", "then"]

# Character corrupt
cum_char_distribution = {0.117402: 'e', 0.207523: 'a', 0.290041: 't', 0.365872: 'i', 0.439843: 'n', 0.512675: 'o', 0.581933: 'r', 0.648057: 's', 0.691402: 'h', 0.734662: 'l', 0.77221: 'd', 0.808792: 'c', 0.835204: 'm', 0.861349: 'u', 0.883286: 'f', 0.905098: 'g', 0.926057: 'p', 0.943347: 'y', 0.959608: 'b', 0.974858: 'w', 0.985132: 'v', 0.992649: 'k', 0.995278: 'j', 0.997384: 'x', 0.999023: 'z', 1: 'q'}
character_percentage = 0.005
punctuations = { # The distribution of punctuation corruptions
  0.05: "",
  0.10: ":",
  0.15: ";",
  0.30: "!", 
  0.45: "?", 
  0.70: ",", 
  1: "."
}
punct_percentage = 0.5 # How often punctuation gets corrupted
