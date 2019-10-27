# Question 6: Given a list of numbers, Iterate it and print only those numbers which are divisible of 5
import sys

def ss(num):
   for i in num:
      if (i%5==0):
         print(i)

num=[10, 20, 30, 15, 19]

ss(num)
