#Question 6: Generate a random Password which meets the following conditions
#Password length must be 10 characters long.
#It must contain at least 2 upper case letter, 2 digits, and 2 special symbols.

import sys
import string
import random

def password(strLength=10):
    specialChar= string.ascii_letters+string.digits+string.punctuation 
    return ''.join(random.choice(specialChar) for char in range(strLength))

print("the password is: ", password(10))
