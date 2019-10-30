#Exercise Question 7: String characters balance Test
#We’ll say that a String s1 and s2 is balanced if all the chars in the string1 are there in s2. characters position doesn’t matter.
#stringBalanceCheck(yn, Pynative) = True
import sys

def balancedStr(S1,S2):
    ss=[]
    nn=[]

    
    for char in S1:
        if char in S2:
           ss.append(char)      
        else:
           nn.append(char)
  
    
    if (nn !=[]):
      return False
    else:
      return True
                     
        
S1= "ynz"
S2= "Pynative"

print(S1, S2, balancedStr(S1,S2))
           


