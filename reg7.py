#Write a Python program to search some literals strings in a string. Go to the editor
#Sample text : 'The quick brown fox jumps over the lazy dog.'
#Searched words : 'fox', 'dog', 'horse'
import re
def textMach(text):

    pattern='\Bo\B'
    #for i in text:
    if re.search(pattern,text):
        
        return True
    else:
        return False
print(textMach('The quick brown fox jumps over the lazy dog.'))
