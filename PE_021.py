'''
Brute force was easy, but I'll tell you what's hard,
Guessing you must perfect numbers discard.
'''

def sum_of_divisors(n):
    rolling_sum = 1
    for i in range(2,int(n**.5)+2):
        if n % i == 0:
            rolling_sum += i
            rolling_sum += n/i
    return rolling_sum

def sum_of_amicables_under(n):
    amicables = []
    tried = []
    for i in range(1,n):
        s = sum_of_divisors(i)
        if s not in tried:
            t = sum_of_divisors(s)
            if t == i and t!=s:
                amicables.append(t)
                amicables.append(s)
            tried.append(t)
        tried.append(s)
    print amicables

    return sum(set(amicables))

if __name__ == '__main__':
    print sum_of_amicables_under(10000)