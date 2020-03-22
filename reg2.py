import re

def matchZero(text):
    pattern='ab+?'
    if re.search(pattern,text):
        return 'Found match'
    else:
        return 'not match found'

print(matchZero('ac'))
print(matchZero('abb'))
print(matchZero('abc'))

