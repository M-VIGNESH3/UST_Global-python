# Write a Python program that uses reduce() 
# to find the greatest common divisor (GCD) of a list of numbers.

from functools import reduce
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

l=[16,8,80,40]
print("list is ",l)
r = reduce(gcd,l)
print("gcd is ",r)
