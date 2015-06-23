__author__ = 'louispotok'

def is_prime(n,prime_list):
    for i in prime_list:
        if i <= int(n**.5):
            if n%i == 0:
                return False
        else:
            break
    return True


def calc_nth_prime(n): #289 ms
    prime_list = []
    candidate = 2

    while len(prime_list)<n:
        if is_prime(candidate, prime_list):
            prime_list.append(candidate)

        candidate += 1
    return prime_list[-1]

## from the solution
def is_prime_prime(n):
    if n == 1:
        return False
    elif n<4:
        return True
    elif n%2 == 0:
        return False
    elif n<9:
        return True
    elif n%3 ==0:
        return False
    else:
        r = int(n**.5)
        f = 5
        while f<=r:
            if n%f == 0:
                return False
            if n%(f+2) == 0:
                return False
            f += 6
        return True

def calc_nth_prime_prime(n): #122 ms
    count = 1
    candidate = 1
    while count <n:
        candidate +=2
        if is_prime_prime(candidate):
            count +=1
    return candidate