#Question 9: Roll dice in such a way that every time you get the same number
#Dice has 6 number(from 1 to 6). Roll dice in such a way that every time you must get same output number. do this 5 times.

import sys
import random

#for i in range(6):
#    random.seed( 6 )
#    num= random.randint(1,6)
#    print("random character form text: ", num)

#########################another solution

dice=[1,2,3,4,5,6]

for i in dice:
    random.seed(25)
    num=random.choice(dice)
    print(num)
   
