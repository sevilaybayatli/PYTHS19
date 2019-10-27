# Question 8: Print the following pattern
import sys

def tringle (num):
     for n in range (num):
         for i in range (n):
             print(n, end=" ")
         print("\n")

tringle(10)
