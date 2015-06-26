'''
I feel like a cheater for using python 'sort';
To avoid an off-by-one error I had to contort.
'''

import os
resource_path = os.path.curdir + '/resources/p022_names.txt'



letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letter_scores = {v:i+1 for i,v in enumerate(letters)}

def main():
    with open(resource_path,'r') as f:
        names = f.read().replace('"','').split(',')
    names.sort()
    return sum([(i+1)*name_score(name) for i,name in enumerate(names)])

def name_score(name):
    return sum([letter_scores[letter] for letter in name])

if __name__ == '__main__':
    print main()