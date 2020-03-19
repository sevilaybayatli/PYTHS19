import sys
from functools import reduce
import collections
from inspect import getmodule
from math import sqrt
import json
#Write a Python program to filter the positive numbers from a list.
lls=[23,1,0,-1,-23]
zz=['w','z','l','k']
nl=[]
nz=[]
for i in lls:
    if (i>0):
       nl.append(i)

print(nl)

for j in zz:
    nz.append(j)
print(nz)

s=[2,3,6]
print(s[0]*s[0]+s[1]*s[1]+s[2]*s[2])
print(s[1]*s[1])
print(s[2]*s[2])
nums=[4,7,8]
print(nums)
print()
product_list=reduce((lambda x,y:x*y),nums)
print(product_list)
#Write a Python program to print Unicode characters.
str = u'\u0050\u0079\u0074\u0068\u006f\u006e \u0045\u0078\u0065\u0072\u0063\u0069\u0073\u0065\u0073 \u002d \u0077\u0033\u0072\u0065\u0073\u006f\u0075\u0072\u0063\u0065'
print()
print(str)
print()

str1="python"
str2="python"
print("\n memory location of str2 ", hex(id(str2)))
print("\n memory location of str1 ", hex(id(str1)))
print()

nums=[30,10,34,90,20]
for x in nums: print(x)
print()
    
#Write a Python program to format a specified string to limit the number of characters to 6. 

s= "sevilay"

print('%.5s'%s)

try:
   x=1
except NameError:
   print("the variable is not defined")
else:
   print("variable is defined")

try:
   y
except NameError:
   print("variable is not defined")
else:
   print("variable is defined")
n=20
d={"x":200}
l=[4,5,6]
t=(1,2,3)
print(type(n)())
print(type(d)())
print(type(l)())
print(type(t)())
#Write a Python program to determine the largest and smallest integers, longs, floats.
I=[2,3,6,8,9]
f=[2.3,5.1,5.5,9.2]
print(I)
print(f)
print(min(I)," ",min(f))
print(max(I)," ", max(f))

s=[9,2,3,1,5,6,7,4]
print(sum(collections.Counter(s).values()))


print(getmodule(sqrt))
#Write a Python program to check if lowercase letters exist in a string.
s="sevilay"
if s.islower():
   print("there is lowercase letter in a string")

else:
   print("there is not any lowercase letter exist in a string")   
print(json.dumps({'Alex': 1, 'Suresh': 2, 'Agnessa': 3}))
var_list=['a','b','c']

x,y,z=(var_list+[None]*3)[:3]
print(x,y,z)
var_list=[10.2,34.8]
x,y=(var_list+[None]*2)[:2]
print(x,y)
print("input the values of x&y")
x,y=map(int,input().split())
print("the integer values",x,y)
print()



   
    
