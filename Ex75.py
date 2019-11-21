import sys
#Write a Python program to test whether all numbers of a list is greater than a certain number. 
liss=[4,5,1,2,3,9]
La=8
s=0
for i in liss:
  if liss[i]>La:
     s+=1
     if (s>0):
        print("not all numbers of list not greater than 8")
        break;
     else:
        print("all numbers less than 8")
      


