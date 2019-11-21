import sys
#Write a Python program to count the number occurrence of a specific character in a string.

s="coconut"
z=''
nu=0
l='c'
for i in s:
   z=i
   if z==l:
      nu+=1
   z=''
print("the number occurrence of c in that string = ",nu)
   

print()
print(ord('a'))
print(ord('A'))
print(ord('1'))
print(ord('B'))
print(ord('@'))
print(ord('#'))
print()

#Given variables x=30 and y=20, write a Python program to print t "30+20=50".
print()
x=30
y=20
print("\n%d+%d=%d" % (x,y, x+y))
