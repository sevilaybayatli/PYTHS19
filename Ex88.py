import sys
import random
#Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.

#letters = ['a', 'e', 'i', 'o', 'u']
#for j in range(5):   
 #  for i in letters:
 #      print(random.choice(letters), end= " ")

  # print()

char_list=['a', 'e', 'i', 'o', 'u']
random.shuffle(char_list)
print(''.join(char_list))



   
