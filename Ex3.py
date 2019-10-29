#Exercise Question 2: Given 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1
#appendMiddle("Chrisdem", IamNewString) → "ChrIamNewStringisdem"
import sys
def merging(s1,s2):

    k= int(len(s1)/2)
    print(s1[:k-1:]+s2+s1[k-1:])

s1= input("enter first string: ")
s2= input("enter second string: ")

merging(s1,s2)
