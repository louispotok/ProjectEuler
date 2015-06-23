__author__ = 'louispotok'

def divis_by_range(n,m):
    for i in range(1,m+1):
        if n%i == 0:
            continue
        else:
            return False
    return True

def brute_force(numb_to_check): #very slow
    n=numb_to_check
    while not divis_by_range(n, numb_to_check):
        n+=1
    return n


def only_check_mults_of_highest(numb_to_check): #11.5 seconds
    n=numb_to_check
    while not divis_by_range(n, numb_to_check):
        n+=numb_to_check
    return n

def divis_by_range_backwards(n,m):
    for i in range(1,m+1)[::-1]:
        if n%i == 0:
            continue
        else:
            return False
    return True

def only_check_mults_of_highest_backwards(numb_to_check): #slower! 12.1s
    n=numb_to_check
    while not divis_by_range_backwards(n, numb_to_check):
        n+=numb_to_check
    return n

def is_prime(n):
    for i in range(2,int(n**.5)+1):
        if n%i == 0:
            return False
    return True


def only_prime_mults(numb_to_check): #aha 45.2 µs
    primes = [i for i in range(2,numb_to_check) if is_prime(i)]
    prime_mult = reduce(lambda x,y: x*y, primes)
    n=prime_mult
    while not divis_by_range(n, numb_to_check):
        n+=prime_mult
    return n