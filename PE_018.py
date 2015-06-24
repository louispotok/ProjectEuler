'''
This problem will not bother you,
If you're blind to every row but two,
Once you solve that simple case,
Then the next row, can you face.
Line by line, and piece by piece,
Find the higher sum until you cease.
'''

def highest_sum_path(t):
    '''
    t a list of list of ints
    '''
    if len(t) == 1:
        return [max(t[0])]
    else:
        return combine(highest_sum_path(t[:-1]), t[-1])

def combine(a,b):
    '''
    a,b : each a list of ints

    '''
    assert len(b) - 1 == len(a)
    # if len(a) == 1:
    #     return [a[0]+b[0],a[0]+b[1]]
    max_paths = []
    for i,v in enumerate(b):
        if i == 0:
            max_paths.append(a[0] + v)
        elif i == len(a):
            max_paths.append(a[-1] + v)
        else:
            max_paths.append(max([a[i-1]+v,a[i]+v]))
    return max_paths

def sanitize_input(s):
    strings = [i.split() for i in s.split('\n')]
    return filter(None,[[int(i) for i in j] for j in strings])

def main(s):
    return max(highest_sum_path(sanitize_input(s)))

problem_input = '''
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
 '''

if __name__=='__main__':
    print main(problem_input)