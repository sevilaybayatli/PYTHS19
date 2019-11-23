import sys
#Write a Python program to input a number, if it is not a number generate an error message.
while True:
   try:
      a=int(input("enter a number: "))
      #break
   except ValueError:
      print("\n It is not a number")
      print()

