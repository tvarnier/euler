def sum_square_difference(l):
    return (sum(range(1, l + 1)) ** 2) - sum(i ** 2 for i in range(1, l + 1))

if __name__ == '__main__':
    print(sum_square_difference(100))