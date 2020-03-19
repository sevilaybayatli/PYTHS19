import sys
import json
print("enter the integer values")
x,y=map(int,input().split())
print("the integer values is ", x,y)
#Write a Python program to print a variable without spaces between values.
x="30"
v=json.dumps(x)
print("the variable of x",v)
y=3
print('the value of x "{}"'.format(y))

