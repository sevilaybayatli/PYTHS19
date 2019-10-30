#Exercise Question 5: Given a string input Count all lower case, upper case, digits, and special symbols
#input_str = "P@#yn26at^&i5ve"
#Total counts of chars, digits,and symbols Chars = 8 Digits = 3 Symbol = 4
import sys
inputStr="P@#yn26at^&i5ve"
sml=0
cap=0
digit=0
say=0
for char in inputStr:
    if char.islower():
       sml+=1
    elif char.isupper():
        cap+=1
    elif char.isdigit():
      digit+=1
    else:
      say+=1


print("loweChar= ", sml, "upperChar= ", cap, "number of digits= ", digit, "nmbers: ", say)
      
