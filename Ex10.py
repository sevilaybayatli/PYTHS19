#Exercise Question 10: Given an input string, count occurrences of all characters within a string
#count("pynativepynvepynative") = {'p': 3, 'y': 3, 'n': 3, 'a': 2, 't': 2, 'i': 2, 'v': 3, 'e': 3}

import sys 

inputStr="pynativepynvepynative"
countDict=dict()
for char in inputStr:
     count=inputStr.count(char)
     countDict[char]=count

print(countDict)

