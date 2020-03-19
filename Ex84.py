import sys
import os, platform
#Write a Python program to find the operating system name, platform and platform release date.
print("the opersating system name")
print(os.name)
print("the platform system")
print(platform.system())
print("the platform release")
print(platform.release())
print(isinstance(25,int) or (isinstance("25",str)))
print(isinstance([25],int))
print(isinstance(["25"],str))
print(isinstance("25",str) or (isinstance("25",str)))
#Write a Python program to test if a variable is a list or tuple or a set.
x=('tuple', False, 3.2,1)

if type(x) is list:
    print("the variable is a list")
elif type(x) is set:
    print("the variable is a set")
elif type(x) is tuple:
    print("the variable is a tuple")
else:
    print("Neither a list or tuple or set")
