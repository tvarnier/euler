def sum_diagonals_spiral(dim):
    i = 0
    current = 1
    sum = 1
    add = 0

    while current != dim * dim:
        if i % 4 == 0:
            add += 2
        current += add
        sum += current
        i += 1

    return sum

if __name__ == "__main__":
    print(sum_diagonals_spiral(1001))