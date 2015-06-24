'''
Two possible approaches:
    1. Recursive -- you can collapse multiple lines into a set of:
        starting position, ending position, max path between them.
        so just add lines to it.
    2. Genetic algorithm?
'''

def highest_sum_path(t):
    '''
    t a triangle
    '''
    if number_rows(t) == 1:
        return max_path(t)
    else:
        return combine(highest_sum_path(child(t)), last_row(t))

