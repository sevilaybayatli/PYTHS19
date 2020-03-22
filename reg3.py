import re
# Write a Python program that matches a string that has an a followed by zero or one 'b'.


def matchZero(text):
    pattern='ab?'
    if re.search(pattern,text):
        return 'Found match'
    else:
                                                                                                                                                                                                                                                                                                               
        return 'not match found'

print(matchZero('ac'))
print(matchZero('abb'))
print(matchZero('abc'))
