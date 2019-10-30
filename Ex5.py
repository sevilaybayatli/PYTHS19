#Exercise Question 4: arrange String characters such that lowercase letters should come first
#input_String = PyNaTive
#arranging characters giving precedence to lowercase letters
#aeiNPTvy

#arranging characters giving precedence to lowercase letters:
#yaivePNT
#import sys
#def diverseChar(txt):
#   sml=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
   #cap=[A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]
#   s=" "
#   p=" "
 #  for i in (txt):
  #     if i in sml:
  #       z=s+i
       #else:
         
         #p.append(i)
   #z=s.append(c)
  # print("new string is: ", z)# "capital characters is: ", p)




#txt=input("enter a combination of string: ")

#diverseChar(txt)

import sys

inputStr= "PyNaTiVe"

lower=[]
upper=[]

for char in inputStr:
     if char.islower():
         lower.append(char)
     else:
         upper.append(char)
 

newStr= "".join(lower+upper)
print("the charcters after arrange them")
print(newStr)


   
