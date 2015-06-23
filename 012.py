__author__ = 'louispotok'


def count_divisors(n): #4.51 s
    divisor_set = set([])
    for i in range(1,int(n**.5)+2):
        if n%i == 0:
            divisor_set.add(i)
            divisor_set.add(n/i)
    return len(divisor_set)

def count_divisors_2(n): #4.59 s
    divisor_list = []
    for i in range(1,int(n**.5)+2):
        if n%i == 0:
            divisor_list.append(i)
            divisor_list.append(n/i)
    return len(set(divisor_list))

def count_divisors_3(n): #4.81 s
    divisor_list = []
    for i in range(1,int(n**.5)+2):
        if n%i == 0 and i not in divisor_list:
            divisor_list.extend([i,n/i])
    return len(divisor_list)

def count_divisors_4(n):
    divisor_list = []
    for i in range(1,int(n**.5)+2):
        if n%i == 0 and i not in divisor_list:
            divisor_list.append(i)
            divisor_list.append(n/i)

def solution(n):

    tri_numb = 1
    count = 2
    while count_divisors_4(tri_numb) <=n:
        tri_numb += count
        count += 1
    return tri_numb