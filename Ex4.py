#Exercise Question 4: arrange String characters such that lowercase letters should come first
#mixString("America", "Japan") = ""AJrpan"
import sys

def mixStr(s1,s2):

   k1=int(len (s1)/2)
   k2=int(len (s2)/2)
   E1= int(len (s1)-1)
   E2= int(len (s2)-1)
   B1=s1[0]
   B2=s2[0]
   print("new string is: ", B1+B2+s1[k1]+s2[k2]+s1[E1]+s2[E2])




s1=input("enter first string: ")
s2=input("enter second string: ")

mixStr(s1,s2)
