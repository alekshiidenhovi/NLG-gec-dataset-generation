import ssl
import nltk
import random

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
    
nltk.download("omw-1.4", quiet=True)
from pattern.en import tag, comparative, superlative, conjugate, singularize, pluralize

import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from settings import articles, article_percentage

def corrupt_adjective(adjective: str) -> str:
    """Added extra comparative or superlative form to the adjective.
    
    Parameters
    ----------
    adjective (str): Adjective to be corrupted
    
    Returns
    -------
    corrupted_adjective (str): Corrupted adjective"""
    
    pos_tag = tag(adjective)[0][1]
    assert pos_tag.startswith("JJ"), f"Word is not an adjective! ({pos_tag})"
    
    if pos_tag == "JJ": # normal
        if random.uniform(0, 1) <= 0.5:
            return comparative(adjective)
        else:
            return superlative(adjective)
    elif pos_tag == "JJR": # comparative
        if adjective.endswith("er"):
            return adjective.rstrip("er")
        else:
            return adjective
    else: # superlative
        if adjective.endswith("est"):
            return adjective.rstrip("est")
        else:
            return adjective


def corrupt_article(article: str) -> str:
    """Corrupts an article by either replacing it with a random article.
    
    Parameters
    ----------
    article (str): Article (a, an, the)
    
    Returns
    -------
    corrupted_article (str): Corrupted article"""
    
    assert article in articles, f"Word is not an article! {article}"
    
    if article == "a":
        if random.uniform(0, 1) <= article_percentage:
            return "an"
        else:
            return "the"
    elif article == "an":
        if random.uniform(0, 1) <= article_percentage:
            return "a"
        else:
            return "the"
    else:
        if random.uniform(0, 1) <= 0.5:
            return "a"
        else:
            return "an"


def corrupt_noun(noun: str) -> str:
    """Pluralize singular noun, singularize plural nouns.
    
    Parameters
    ----------
    noun (str): Noun to be corrupted
    
    Returns
    -------
    corrupted_noun (str): Corrupted noun"""
    
    pos_tag = tag(noun)[0][1]
    assert pos_tag.startswith("NN"), f"Word is not a noun! ({pos_tag})"
    
    if tag(noun)[0][1].endswith("S"):
        return singularize(noun)
    else:
        return pluralize(noun)


def corrupt_verb(verb: str) -> str:
    """Corrupt verb tenses, person and number.
    
    Parameters
    ----------
    verb (str): Verb to be corrupted
    
    Returns
    -------
    corrupted_verb (str): Corrupted verb"""
    
    pos_tag = tag(verb)[0][1]
    assert pos_tag.startswith("VB"), f"Word is not a verb! ({pos_tag})"
    
    aliases = ["inf", "1sg", "2sg", "3sg", "pl", "part", "1sgp", "2sgp", "3gp", "ppl", "ppart"]
    idx = random.randint(0, len(aliases) - 1)
    
    return conjugate(verb, aliases[idx])


def corrupt_POS(word: str) -> str:
    """Corrupt words based on POS-tags.
    
    Parameters
    ----------
    word (str): Word to be corrupted
    
    Returns
    corrupted_word (str): Corrupted word"""
    
    pos_tag = tag(word)[0][1]
    
    if word in articles:
        return corrupt_article(word)
    elif pos_tag.startswith("JJ"):
        return corrupt_adjective(word)
    elif pos_tag.startswith("NN"):
        return corrupt_noun(word)
    elif pos_tag.startswith("VB"):
        return corrupt_verb(word)
    else:
        return word


if __name__ == '__main__':
    print("Adjectives")
    print(f"big: {corrupt_POS('big')}")
    print(f"bigger: {corrupt_POS('bigger')}")
    print(f"biggest: {corrupt_POS('biggest')}")
    print("---------------")
    
    print("Articles")
    print(f"a: {corrupt_POS('a')}")
    print(f"an: {corrupt_POS('an')}")
    print(f"the: {corrupt_POS('the')}")
    print("---------------")
    
    print("Nouns")
    print(f"child: {corrupt_POS('child')}")
    print(f"children: {corrupt_POS('children')}")
    print(f"sheep: {corrupt_POS('sheep')}")
    print(f"people: {corrupt_POS('people')}")
    print("---------------")
    
    print("Verbs")
    print(corrupt_POS('be'))
    print(corrupt_POS('be'))
    print(corrupt_POS('be'))
    print(corrupt_POS('be'))
    print(corrupt_POS('be'))
    print(corrupt_POS('be'))
    print(corrupt_POS('be'))
    print(corrupt_POS('be'))
    print("---------------")
    