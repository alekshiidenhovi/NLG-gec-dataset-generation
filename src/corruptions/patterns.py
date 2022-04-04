import ssl
import nltk

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
    
nltk.download("omw-1.4")


# Pluralization / singularization
# Article corruption: wrong one, dropping out
# Verbs: 
# - adding / dropping s in third-person
# - tense corruption
# - conditional / future tense mixup
# -v
# Nouns:
# - comparative, superlative
# - 
    
from pattern.en import (
    article, referenced, INDEFINITE, DEFINITE, tag, comparative, superlative, conjugate
)

if __name__ == '__main__':
    # Indefinite article
    # print(article("dog"))
    # print(article("apple"))
    
    # print(referenced("dog", article=DEFINITE))
    # print(referenced("", article=INDEFINITE))
    # sentence = "I went to the bank to get the money and then I went to lie on a river bank."
    
    # for word, pos in tag(sentence):
    #     # if pos == "VB":
    #     print(pos)
    print(conjugate("be", "VBP"))
