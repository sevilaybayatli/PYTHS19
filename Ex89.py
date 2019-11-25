import sys
#Write a Python program to remove and print every third number from a list of numbers until the list becomes empty.

s=[1,2,3,4,5]
for i in s:
    print(s[2])
    s.remove(s[2])
    if len(s)==2:
       print(s[1])
       s.remove(s[1])
    if len(s)==1:
       print(s[0])
       s.remove(s[0])

print("the list is empty ", s)
   
