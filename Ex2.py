# Exercise Question 1: Given a string of odd length greater 7, return a string made of the middle three chars of a given String
#Original String is JhonDipPeta
#Middle three chars are Dip
#Original String is Jasonay
#Middle three chars are son

import sys

#def newstr(text):
   
#        print(text[2:5])

#newstr("sevilay")


def newstr(text):
    k= int(len(text)/2)
    print(text[k-1:k+1])

text= input ("enter a string")

newstr(text)
        
