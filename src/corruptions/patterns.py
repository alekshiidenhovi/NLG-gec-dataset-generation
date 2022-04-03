import ssl
import nltk

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
    
nltk.download("omw-1.4")

from pattern.en import pluralize, singularize, lemma, lexeme

if __name__ == '__main__':
    # print("Hello world")
    # print(pluralize("cat"))
    # print(singularize("children"))
    print(lemma("purring"))
    print(lexeme("purr"))