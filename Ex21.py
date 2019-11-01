#Question 1: Generate 3 random integers between 100 and 999 which is divisible by 5
import sys
import random

for i in range(3):
   number=random.randrange(100,999,10)
   print("the raondm number which is divisible by 5: ", number)

