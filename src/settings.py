# Sentence corrupt
sentence_percentage = 0.7

# Word corrupt
masking = 0.04
deletion = 0.08
insertion = 0.10
seq_threshold = 8
random_tokens = ["a", "an", "the", "on", "in", "out", "at", "to", "from",
                "of", "off", "for", "with", "as", "and", "but", "then"]

# Character corrupt
alphabets = list(set("abcdefghijklmnopqrstuvwxyz"))
punctuations = {
  0.05: "",
  0.10: ":",
  0.15: ";",
  0.30: "!", 
  0.45: "?", 
  0.70: ",", 
  1: "."
}