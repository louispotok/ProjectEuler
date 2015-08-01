'''
If you wish to know the correct amount,
Take heed, young one, and from zero count.
'''

def get_nth_arrangement(n,elements):
    'n is zero-indexed, elements must be sorted'
    if len(elements) == 1:
        return elements
    number_arrangements_after = factorial(len(elements)-1)
    first_element = elements[n/number_arrangements_after]
    number_arrangements_used = elements.index(first_element)*number_arrangements_after
    return [first_element] + get_nth_arrangement(n-number_arrangements_used,
                                               [i for i in elements if i != first_element])

def factorial(n):
    if n <=1:
        return n
    else:
        return n * factorial(n-1)

def string_list(x):
    return [str(i) for i in x]

if __name__=='__main__':
    print ''.join(string_list(get_nth_arrangement(1000000-1,
                              range(10))))