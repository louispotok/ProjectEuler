__author__ = 'louispotok'

def fibo_sum_of_even_vals_up_to_n(n):
    a = 1
    b = 2
    rolling_sum = 2
    while a<n:
        a+=b
        if a>n:
            break
        if a%2 == 0:
            rolling_sum+=a
        if b>=n:
            break
        else:
            b+=a
            if b%2 == 0:
                rolling_sum += b
    print rolling_sum