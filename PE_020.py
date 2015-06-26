'''
Another problem that is no fun,
I'm praying for better on the next one.
'''
from PE_004 import get_digits


def factorial(n):
    product = 1
    for i in range(1,n+1):
        product *= i
    return product

if __name__ == '__main__':
    print sum(get_digits(factorial(100)))