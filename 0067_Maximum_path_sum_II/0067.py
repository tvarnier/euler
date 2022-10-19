"""
https://projecteuler.net/problem=67

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
"""

def maximum_path_sum(a):
    max = 0
    for row, line in enumerate(a):
        for col, nbr in enumerate(line):
            if row > 0:
                if col == 0:
                    a[row][col] += a[row - 1][col]
                else:
                    a[row][col] += a[row - 1][col - 1] if (col == len(line) - 1 or a[row - 1][col - 1] > a[row - 1][col]) else a[row - 1][col]
            if row == len(a) - 1 and a[row][col] > max:
                max = a[row][col]
    return max

if __name__ == '__main__':

    text_file = open("triangle.txt", "r")
    s = text_file.read()
    text_file.close()

    a = []
    for line in s.splitlines():
        a.append([int(nbr) for nbr in line.split(" ")])

    print(maximum_path_sum(a))