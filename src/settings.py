# Main
MAX_SEQ_LENGTH = 40 # Maximum amount of words
training_amount = 100000 # Amount of training samples
validation_amount = 100 # Amount of validation samples

# Pattern corrupt


# Sentence corrupt
sentence_percentage = 0.7 # How many sentences get corrupted

# Word corrupt
word_masking = 0.03 # Fraction of words masked
word_deletion = 0.07 # ... deleted
word_insertion = 0.10 # ... inserted
seq_threshold = 8 # Sequence length threshold for word corruptions
cum_word_distribution = {0.193441: 'the', 0.280574: 'and', 0.363159: 'of', 0.445062: 'in', 0.501302: 'a', 0.551774: 'to', 0.57743: 'was', 0.602879: 'as', 0.62581: 'on', 0.648421: 'for', 0.670956: 'he', 0.693461: 'is', 0.714285: 's', 0.734425: 'with', 0.752374: 'by', 0.768667: 'it', 0.783793: 'at', 0.79802: 'from', 0.81148: 'that', 0.824133: 'his', 0.834153: 'which', 0.843898: 'an', 0.85187: 'this', 0.859493: 'but', 0.867001: 'were', 0.874116: 'or', 0.880962: 'she', 0.887599: 'th', 0.894177: 'are', 0.900746: 'after', 0.907238: 'who', 0.913499: 'also', 0.919435: 'be', 0.925311: 'one', 0.931012: 'new', 0.936532: 'first', 0.942023: 'they', 0.947106: 'had', 0.951961: 'their', 0.956806: 'her', 0.961562: 'its', 0.966272: 'has', 0.970937: 'not', 0.975539: 'when', 0.980004: 'two', 0.984182: 'born', 0.988336: 'there', 0.992366: 'during', 0.996187: 'all', 1: 'have'}

# Character corrupt
cum_char_distribution = {0.117402: 'e', 0.207523: 'a', 0.290041: 't', 0.365872: 'i', 0.439843: 'n', 0.512675: 'o', 0.581933: 'r', 0.648057: 's', 0.691402: 'h', 0.734662: 'l', 0.77221: 'd', 0.808792: 'c', 0.835204: 'm', 0.861349: 'u', 0.883286: 'f', 0.905098: 'g', 0.926057: 'p', 0.943347: 'y', 0.959608: 'b', 0.974858: 'w', 0.985132: 'v', 0.992649: 'k', 0.995278: 'j', 0.997384: 'x', 0.999023: 'z', 1: 'q'}
character_percentage = 0.007 # Fraction of characters corrupted
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
char_replacement = 0.7
punct_percentage = 0.5 # How often punctuation gets corrupted
