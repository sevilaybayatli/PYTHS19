import sys
import random
#Write a Python program to check the sum of three elements (each from an array) from three arrays is equal to a target value. Print all those three-element combinations.
#Sample data:
#/*
#X = [10, 20, 20, 20]
#Y = [10, 20, 30, 40]
#Z = [10, 30, 40, 20]
target = 70
#*/
hit=[]
X = [10, 20, 20, 20]
Y = [10, 20, 30, 40]
Z = [10, 30, 40, 20]

for i in X:
  for j in Y:
    for k in Z:
        #l=i+j+k
        if (i+j+k)==target and (i,j,k) not in hit:
           hit.append((i,j,k))
print(set(hit))



result=[]

for i in range(40):
    A=[1,2,3]
    random.shuffle(A)
    if A not in result:
       result.append(A)
print(result)

X = [1,2,3]
result=[]
for a in X:
for b in X:
for c in X:
if (a+b+c)==sum(X) and a!=b!=c:
perm=(a,b,c)
result.append(perm)
print(result)
    
               


