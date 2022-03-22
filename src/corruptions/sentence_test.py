from sentence import sentence_corrupt
import sys
sys.path.append("../src")
from load_wikipedia import load_wikipedia

# sentence = "A transformer is a deep learning model that adopts the mechanism of self-attention, differentially weighting the significance of each part of the input data."

# print(sentence_corrupt(sentence, 1, 0.1))
# print(sentence_corrupt(sentence, 1, 0.2))
# print(sentence_corrupt(sentence, 1, 0.3))
# print(sentence_corrupt(sentence, 1, 0.5))
# print(sentence_corrupt(sentence, 1, 0.9))

# print(load_wikipedia())

for sentence in load_wikipedia():
    # filtered = list(map(lambda x: , sentence))
    print(sentence_corrupt(sentence, 0.7))