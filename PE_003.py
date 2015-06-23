__author__ = 'louispotok'

def is_prime(n):
    i=0
    for i in range(2,int(n**.5)+1):
        if n%i == 0:
            return False
    return True


def largest_prime_factor(n):
    candidate = 1
    for i in range(1,int(n**.5)+1):
        if n%i == 0 and is_prime(i):
            candidate=i
    return candidate

