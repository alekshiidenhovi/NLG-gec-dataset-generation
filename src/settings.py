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
word_percentage = 0.15 # Fraction of words corrupted
word_masking = 0.1 # Fraction of corruptions masked
word_deletion = 0.3 # ... deleted
word_insertion = 0.5 # ... inserted
word_swap = 0.65 # ... swapped
cum_word_distribution = {0.159024: 'the', 0.24421: 'and', 0.322756: 'of', 0.386656: 'in', 0.438544: 'to', 0.488117: 'a', 0.521234: 'was', 0.548375: 'is', 0.569344: 'as', 0.589777: 'for', 0.608854: 's', 0.627591: 'on', 0.646313: 'with', 0.663082: 'by', 0.676456: 'that', 0.689313: 'at', 0.701685: 'from', 0.713382: 'he', 0.724409: 'his', 0.734962: 'which', 0.743755: 'an', 0.75156: 'were', 0.759008: 'but', 0.766377: 'are', 0.773602: 'it', 0.780103: 'who', 0.78654: 'or', 0.792711: 'also', 0.798599: 'has', 0.804446: 'be', 0.810272: 'first', 0.815935: 'had', 0.820966: 'th', 0.825854: 'new', 0.83066: 'their', 0.835294: 'this', 0.839908: 'one', 0.844273: 'her', 0.848586: 'its', 0.852842: 'not', 0.856792: 'after', 0.860697: 'two', 0.864601: 'have', 0.868279: 'she', 0.871868: 'been', 0.87539: 'where', 0.878903: 'they', 0.882353: 'when', 0.88553: '-', 0.888582: 'into', 0.891591: 'may', 0.894593: 'other', 0.897577: 'including', 0.900486: 'time', 0.903376: 'years', 0.90615: 'all', 0.908753: 'such', 0.911316: 'school', 0.913859: 'more', 0.916366: 'during', 0.918848: 'then', 0.921316: 'season', 0.923755: 'would', 0.926193: 'only', 0.928624: 'born', 0.931036: 'while', 0.933369: 'over', 0.935685: 'up', 0.93795: 'between', 0.940178: 'city', 0.942382: 'there', 0.944563: 'made', 0.946708: 'most', 0.94885: 'used', 0.950986: 'world', 0.953108: 'him', 0.955222: 'year', 0.957299: 'united', 0.959368: 'three', 0.961412: 'later', 0.963438: 'about', 0.96544: 'out', 0.96744: 'film', 0.969422: 'american', 0.971404: 'state', 0.973383: 'can', 0.975353: 'national', 0.977318: 'being', 0.979245: 'march', 0.981171: 'university', 0.983089: 'became', 0.985007: 'until', 0.986914: 'some', 0.988805: 'second', 0.99069: 'before', 0.992574: 'team', 0.994437: 'part', 0.996295: 'under', 0.998151: 'known', 1: 'through'}


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
char_replacement = 0.7
punct_percentage = 0.5 # How often punctuation gets corrupted
