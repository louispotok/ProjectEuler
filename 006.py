__author__ = 'louispotok'

def square_of_sums(n):
    return (reduce(lambda x,y: x+y, [i for i in range(1,n+1)]))**2

def sum_of_squares(n):
    return reduce(lambda x,y: x+y**2, [i for i in range(1,n+1)])

def diff(n): #38.1 µs per loop
    return square_of_sums(n) - sum_of_squares(n)
