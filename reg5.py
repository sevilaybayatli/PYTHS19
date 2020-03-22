import re
#Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.
def text_match(text):
        patterns = '^2\w*'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("2he quick brown fox jumps over the lazy dog1"))
print(text_match("Python_Exercises"))

