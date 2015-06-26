
def sum_of_divisors(n):
    rolling_sum = 1
    for i in range(2,int(n**.5)+1):
        if n % i == 0:
            rolling_sum += i
            if n/i != i:
                rolling_sum += n/i
    return rolling_sum

def main():
    abundants = []
    for i in range(1,28124):
        if sum_of_divisors(i) > i:
            abundants.append(i)
    print len(abundants)
    all_sums_of_abundants = set([i+j for i in abundants for j in abundants])
    print list(all_sums_of_abundants)[:5]
    non_sums = set(range(28124)).difference(all_sums_of_abundants)
    print list(non_sums)[:5]
    return sum(non_sums)

if __name__ == '__main__':
    print main()
