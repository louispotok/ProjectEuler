"""
Problem eighteen shows the way,
Look there for help, you'll be okay.
"""

from PE_018 import main
import os


if __name__ == '__main__':
    resource_path = os.path.curdir + '/resources/p067_triangle.txt'
    with open(resource_path,'r') as f:
        problem_input = f.read()
    print main(problem_input)