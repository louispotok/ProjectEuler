__author__ = 'louispotok'

def check_if_prime(prime_list, n):
    for i in prime_list:
        if n%i == 0:
            return False
    return True

def primes_below_n(n):
    prime_list = [2,3]
    i = 6
    while i+1<n:
        for j in [i-1,i+1]:
            if check_if_prime(prime_list,j):
                prime_list.append(j)
        i+=6
    return prime_list

def solution(): #still running AFAIK
    return sum(primes_below_n(2*(10**6)))

solution()

######

def check_if_prime(n):
    for i in range(2,int(n**.5)+1):
        if n%i == 0:
            return False
    return True

def primes_below_n(n):
    prime_list = [2,3]
    i=6
    while i+1<n:
        for j in [i-1,i+1]:
            if check_if_prime(j):
                prime_list.append(j)
        i+=6
    return prime_list

def solution(n):
    return sum(primes_below_n(n))

solution(2*(10**6)) #18.5 s

#######

def is_prime(n):
    for i in range(2,int(n**.5)+1):
        if n%i == 0:
            return False
    return True

#still running
def sieve_of_eratosthenes(n): #see whether it's faster to build the primelist one by one
    composite_list = []
    for i in range(2,n):
        if i not in composite_list:
            j=2
            while i*j < n:
                if i*j not in composite_list:
                    composite_list.append(i*j)
                j+=1
    prime_list = range(2,n)
    for i in composite_list:
        prime_list.remove(i)
    return prime_list

def solution(n):
    return sum(sieve_of_eratosthenes(n))

################

#how about a boolean list, dummy.

def sieve_2(n):
    is_prime = [True] * (n+1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2,n+1):
        if is_prime[i] == True:
            j = 2
            while i*j <= n:
                is_prime[i*j] = False
                j += 1
    return is_prime

def sum_list_indics(list_to_sum):
    return sum([i for i in range(len(list_to_sum)) if list_to_sum[i] == True])

def solution(n): #here we go 1.45 s
    return sum_list_indics(sieve_2(n))