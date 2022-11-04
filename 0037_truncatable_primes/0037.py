import itertools

import math

def is_prime(nbr):
    return sum(1 for div in range(1, round(math.sqrt(nbr) + 1)) if not nbr % div) == 1

def truncatable_primes():
    prenumbers = [1, 2, 3, 5, 7, 9]
    search = set()
    search.add(3)
    search.add(7)

    sum_truncatablePrime = 0

    count = 11
    while count != 0:
        tmp_search = set()
        for pre in prenumbers:
            for s in search:
                nbr = pre * (10 ** len(str(s))) + s

                if not is_prime(nbr):
                    continue

                is_truncatablePrime = True

                for i in range(1, len(str(nbr))):
                    if not is_prime(nbr // (10 ** i)) or not is_prime(nbr % (10 ** i)) or nbr // (10 ** i) == 1 or nbr % (10 ** i) == 1:
                        is_truncatablePrime = False
                        break
                if is_truncatablePrime:
                    sum_truncatablePrime += nbr
                    count -= 1

                tmp_search.add(nbr)
        search = tmp_search
    return sum_truncatablePrime

if __name__ == '__main__':
    print(truncatable_primes())





                