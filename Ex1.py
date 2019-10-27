import sys

def multiplication_or_sum(num1, num2):

  product= num1*num2
  if (product>1000):
    return product

  else:
    return num1+num2

num1= int (input ("enter first number"))
num2= int (input ("enter second number"))

result= multiplication_or_sum(num1, num2)

print("the result: ", result)


