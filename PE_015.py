__author__ = 'louispotok'
'''
 2N times must step your feet,
 before the exit shall you greet.
 exactly N must face the east,
 choose which you like, or loathe the least.

 real	0m0.018s
 user	0m0.010s
 sys	0m0.007s
'''

def combination(n,r):
    return nPr(n,r) / nPr(r,1)

def nPr(n,r):
    product = 1
    for i in range(r+1,n+1):
        product *= i
    return product

def main(n):
    return combination(2*n,n)

if __name__ == '__main__':
    print main(20)