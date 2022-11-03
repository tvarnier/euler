import math

def amicable_number(limit):
    s = 0
    for nbr in range(1, limit):
        sum_divisors = sum([div for div in range(1, nbr) if not nbr % div])
        if sum_divisors > nbr and sum([div for div in range(1, sum_divisors) if not sum_divisors % div]) == nbr:
            s += nbr + sum_divisors
    return s


if __name__ == '__main__':
    print(amicable_number(10000))