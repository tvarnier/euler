def containsAny(str, set):
    return 1 in [c in str for c in set]

def circular_primes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1

    count_circulars = 0
    for p in range(2, n+1):
        if prime[p]:
            if not containsAny(str(p), '024658') or p in [2, 4, 5, 6, 8]:
                is_circular = True
                l = len(str(p))
                tmp = p
                for i in range(l):
                    tmp = (tmp * 10) % (10 ** l) + (tmp // (10 ** (l - 1)))
                    if not prime[tmp]:
                        is_circular = False
                        break
                if is_circular:
                    count_circulars += 1
    return count_circulars

if __name__ == '__main__':
    print(circular_primes(1000000))