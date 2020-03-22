import re
# Write a Python program that matches a string that has an a followed by zero or one 'b'.
# Write a Python program to find the sequences of one upper case letter followed by lower case letters
# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
# Write a Python program that matches a word at the end of string, with optional punctuation.
# Write a Python program that matches a word containing 'z'.
# import re
# Write a Python program that matches a word containing 'z', not at the start or end of the word


def text_match(text):
        patterns = '\Bz\B'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("The quick brown zfox jumps over the laz dog."))
print(text_match("Python Exerzises."))
