import sys
import math

#def diffnum(x):
  
#   if x<=17:
#      return 17-x
#   else:
#      return(x-17)*2

#x=int(input("enter the number: "))

#print(diffnum(x))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#def findnum(num):
#
 # if num in range(100):
  #    print("number in range 100")
  #elif num in range(1000):
   #   print("number in range 1000")
  #elif num in range(2000):
   #   print("number in range 2000")
  #else:
   #  print("the number not in range 100, or 1000, or 2000")

#num=int(input("enter a number: "))

#findnum(num)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#def equality(x1,x2,x3):
#     if(x1==x2 and x2==x3):
#       for i in range(3):
 #          print(x1+x2+x3)



#x1=int(input("enter the first number"))
#x2=int(input("enter the second number"))
#x3=int(input("enter the third number"))

#equality(x1,x2,x3)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#def changestr(str):
#  if (len(str)>=2 and str[:2]=='is'):
 #    return str
 # else:
  #   return 'is'+str
  
   
#str=input("enter a string")

#print(changestr(str))
#~~~~~~~~~~~~~~~~~~~~~~~
#def findnum(L):
#    z=0
#    print(L)
#    for i in L:
#        if i=='4':
#          z=z+1
#    print(z)

#x=input("enter you list numbers: ")
#L=x.split(",")
#findnum(L)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2.

#def strr(s,n):
#   if len(s)<2:
#     print(s*n)
#   else:
#     print(s[:2]*2)
   
    

#s=input("enter the string: ")
#n=int(input("enter the number: "))
#strr(s,n)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def vowelletter(s):
  vowels=['a','e','i','u','o']

  if s in vowels:
     return True
  else:
     return False

x=input("enter the letter ")

print(vowelletter(x))



   
     



