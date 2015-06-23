__author__ = 'louispotok'

def is_palindrome(n):
    n = str(n)
    for i in range(len(n)/2):
        if n[i] != n[-(i+1)]:
            return False
    return True

 #try the other way (mod powers of 10) as well
def get_digits(n, base=10):
    list_digits = []
    while n != 0:
        list_digits.append(n%(base))
        n = (n - n%(base)) / (base)
    return list_digits

def is_palindrome_as_number(n):
    digit_list = get_digits(n)
    n_as_char = ''.join(map(str,digit_list))
    return is_palindrome(n_as_char)

def biggest_palindrome(n):
    candidate = 0
    for i in range(n)[::-1]:
        if i*n < candidate:
            continue
        else:
            for j in range(n)[::-1]:
                new_candidate = i*j
                if new_candidate > candidate and is_palindrome(new_candidate):
                    candidate = new_candidate
    return candidate