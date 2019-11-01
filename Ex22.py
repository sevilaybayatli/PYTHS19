#Question 2: Random Lottery Pick
#Lottery game –  Generate a 100 Lottery tickets and pick two lucky tickets from it as a winner.
#Note you must adhere to the following conditions:
#Lottery number must be 10 digits long.
#All 1000 ticket number must be unique.
#Hint: Generate a random list of 100 numbers. Use random.randrange()  for number generation and random.sample() method to pick lucky 2 tickets.

import sys
import random
listt=[]
k=2
for i in range (100):

    number=(random.randrange(1000000000, 9999999999))
    listt.append(number)

result=random.sample(listt, k)

print("two lucky tickets from it as a winner: ", result)
  


