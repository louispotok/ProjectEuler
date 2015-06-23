__author__ = 'louispotok'

def collatz(n):
    seq = [n]
    while seq[-1] != 1:
        n = seq[-1]
        if n%2 == 0:
            seq.append(n/2)
        else:
            seq.append((3*n)+1 )
    return seq

def longest_collatz(limit): #35.9 s
    candidate = 0
    cand_length = 0
    for i in range(1,limit):
        new_len = len(collatz(i))
        if new_len > cand_length:
            candidate = i
            cand_length = new_len
    return candidate


### attempt 2


def longest_collatz_under_n(n): #3.05 s
    collatz_dict = {1: 0}
    candidate = 0
    cand_length = 0
    for i in range(1,n):
        seq = [i]
        latest = seq[-1]
        while latest not in collatz_dict:
            if latest%2 == 0:
                seq.append(latest/2)
            else:
                seq.append((3*latest) + 1)
            latest = seq[-1]

        if len(seq) + collatz_dict[seq[-1]] > cand_length:
            candidate = i
            cand_length = len(seq) + collatz_dict[seq[-1]] - 1
        for i,v in enumerate(seq):
            if v not in collatz_dict:
                collatz_dict[v] = len(seq) - i + collatz_dict[seq[-1]]

    return candidate, cand_length
