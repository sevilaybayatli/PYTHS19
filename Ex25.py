#Question 5: Generate  random String of length 5
#Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.

import sys
import random
import string

def strrand(stringLength=10):
    letters=string.ascii_lowercase
    #for char in range(stringLength):
        
        #return ''.join(random.choice(letters))
    return ''.join(random.choice(letters) for i in range(stringLength))

print ("Random String is ", strrand() )
print ("Random String is ", strrand(10) )
print ("Random String is ", strrand(30) )
         
         
