#this file contains the core functions implemented in the scientific calculator. extra functions canbe added....
import math

#Square root function
def sqrt(x):
    if x < 0:
        raise ValueError("Cannot take square root of a negative number")
    return math.sqrt(x)

#Factorial function
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    return math.factorial(int(n))

#Log function
def ln(x):
    if x <= 0:
        raise ValueError("Logarithm only defined for positive numbers")
    return math.log(x)

#Power function
def power(x, b):
    return math.pow(x, b)
