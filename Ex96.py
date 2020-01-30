import sys

def sumsval(x, y):
   z=x+y
 

   return z

x=int(input("enter a first number"))
y=int(input("enter a second number"))

print("the result= ", sumsval(x,y))

def find_perimeter(h,w):

   p=2*(h+w)
   return p

h=int(input("enter hight of rectangle"))
w=int(input("enter the width of rectangle"))

print("the perimeter of rectangle= ",find_perimeter(h,w))



