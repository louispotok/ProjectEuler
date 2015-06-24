'''
I thought that there might be a trick,
I wanted to think of myself as slick.
Then I tried the obvious way,
Worked like a charm, to my dismay.
'''

def main(n):
    return sum(get_digits(n))

def get_digits(n, base=10):
    '''
    From my solution to PE_004
    '''
    list_digits = []
    while n != 0:
        list_digits.append(n%(base))
        n = (n - n%(base)) / (base)
    return list_digits

if __name__ == '__main__':
    print main(2**1000)