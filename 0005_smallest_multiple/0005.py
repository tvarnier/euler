"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def smallest_multiple(r):
    res = r[-1]

    while 1:
        res += r[-1]
        for i in r:
            if res % i != 0:
                break
            if i == r[-1]:
                return res
            

if __name__ == '__main__':
    print(smallest_multiple(range(1, 20)))