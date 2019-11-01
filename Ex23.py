#Question 3: Generate 6 digit random secure OTP
import sys
import random
import secrets
secretsGenerator = secrets.SystemRandom()
print("Generating 6 digit random OTP")
otp= secretsGenerator.randrange(100000,9999999)
print("OTP is: ", otp)
