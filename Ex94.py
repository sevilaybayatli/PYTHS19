import sys
# Write a Python program to check the priority of the four operators (+, -, *, /).

__operators__="+-*/"
__paranthesis__="()"
__priority__={'+':0,'-':0, '*':1, '/':1}

def high_priority(operator1,operator2):
    return __priority__[operator1] >= __priority__[operator2]


print(high_priority('+','-'))
print(high_priority('*','-'))
print(high_priority('+','/'))

#Write a Python program to find the median among three given numbers.

nums=[2,5,1]
numb=[2,3,4,1]

def median(n):
   if (len(n)%2>0):
       z=int(len(n)/2)
       return z
   elif (len(n)%2==0):
       z=int(len(n)/2)
       m=z+n[z-1]/2
       return m

print("the median number of these numbers is: ", median(nums))
print("the median number of these numbers is: ", median(numb))

def ndegress(num):
   ans=True
   n,tempn,i=2,2,2
   while ans:
      if str(tempn) in num:
         i+=1
         tempn=pow(n,i)
      else:
         ans=False
   return i-1

print(ndegress("2481632"))
print(ndegress("248163264"))
       
     
