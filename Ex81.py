import sys
from functools import reduce
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
   
    
