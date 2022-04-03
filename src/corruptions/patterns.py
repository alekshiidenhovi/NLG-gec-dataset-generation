import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

from pattern.en import pluralize, singularize

if __name__ == '__main__':
    print("Hello world")
    print(pluralize("cat"))
    print(singularize("children"))