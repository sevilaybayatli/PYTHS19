#Write a Python program to remove leading zeros from an IP address.
#Write a Python program to check for a number at the end of a string.
#Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string
import re
def textMach(text):

    pattern='[0-9]+'
    #for i in text:
    if re.search(pattern,text[1:3]):
        return True
    else:
        return False
text= input("enter a text: ")
print(textMach(text))

    #pattern='\w*[0-9]+$'
    #if re.search(pattern, text):
     #  return ('number at the end of string')
    #else:
     # return("number not at end of string ")

#text=input("Please enter a text: ")
#print(textMach(text))
    
#string = re.sub('\.[0]*', '.', ip)
#print(string)
#ip=str(input("Enter a ip: "))
#print(IPp(ip))
