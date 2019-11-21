import sys
import time
import socket	
# Write a Python program to perform an action if a condition is true. 
# Given a variable name, if the value is 1, display the string "First day of a Month!" and do nothing if the value is not equal.

x=int(input("enter a first number: "))
y=int(input("enter a second number: "))

if x==1:
  print("First day of a Month!")
#Write a Python program to swap two variables.
print()
print("x= ", x, "y= ",y)
z=x
x=y
y=z
print("x= ", x, "y= ",y)

#Write a Python program to check if a string is numeric.
i='123'
try:
 l=float(i)
except(ValueError, TypeError):
 print("\nnot numeric")
print()
print(time.ctime())
print()

host_name = socket.gethostname()
print()
print("Host name:", host_name)
print()

