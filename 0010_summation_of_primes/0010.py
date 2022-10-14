"""
https://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

def summation_of_primes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1

    res = 0

    for p in range(2, n+1):
        if prime[p]:
            res = res + p
    return res

if __name__ == '__main__':
    print(summation_of_primes(2000000))