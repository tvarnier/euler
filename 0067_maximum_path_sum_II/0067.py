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