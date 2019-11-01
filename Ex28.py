# Question 8: Generate random secure token of 64 bytes and random URL
# Python secrets module to generate a secure token
# Python secrets module to generate secure URL

import sys
import random
import secrets
secretsGenerator = secrets.SystemRandom()
numbyte= secrets.token_hex(64)
urll= secrets.token_urlsafe(64)
print("the token in byte: ", numbyte)
print("the token in byte: ", urll)
