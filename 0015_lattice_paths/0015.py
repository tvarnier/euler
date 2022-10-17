"""
https://projecteuler.net/problem=15

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

import math

def lattice_paths(len):
    return (math.factorial(len * 2) / (math.factorial(len) ** 2))  

if __name__ == '__main__':
    print(lattice_paths(20))