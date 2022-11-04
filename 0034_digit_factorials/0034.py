factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

def get_limit():
    sum = factorials[9]
    nbr = 9
    while nbr < sum:
        sum += factorials[9]
        nbr = nbr * 10 + 9
    return sum

if __name__ == '__main__':
    lim = get_limit()

    sum_curious_numbers = 0

    for nbr in range(3, lim):
        sum = 0
        tmp = nbr
        while tmp:
            sum += factorials[tmp % 10]
            tmp = tmp // 10
        if (nbr == sum):
            sum_curious_numbers += nbr

    print(sum_curious_numbers)