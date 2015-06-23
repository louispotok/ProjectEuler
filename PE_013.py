__author__ = 'louispotok'

def decompose_to_digits(n):
    i = 0
    digit_list = []
    while n / (10**i) != 0:
        digit_list.append((n%(10**(i+1)))/(10**(i)))
        i+=1
    digit_list.reverse()
    return digit_list


def first_ten_of_sum(lister): #208 µs per loop
    rolling_sum = 0
    for i in lister:
        rolling_sum += i
    return decompose_to_digits(rolling_sum)[:10]
