__author__ = 'louispotok'

def squares_to_n(n):
    squares = []
    i = 1
    while i**2 < n**2:
        squares.append(i**2)
        i +=1
    return squares

def triplets_that_sum(square_list, n):
    for i in square_list:
        for j in square_list:
            if (((i + j) in square_list)
                and (i**.5 + j**.5 + ((i + j)**.5))==n):
                    return i**.5,j**.5,((i + j)**.5)

def solution(n): #3.07s
    return triplets_that_sum(squares_to_n(n),n)

