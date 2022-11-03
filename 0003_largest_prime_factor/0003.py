def largest_prime_factor(n):
    largest_factor = 1
    i = 2

    while i * i <= n:
        if n % i == 0:
            largest_factor = i
            while n % i == 0:
                n //= i
        i = 3 if i == 2 else i + 2

    if n > 1:
        largest_factor = n

    return largest_factor


if __name__ == '__main__':
    print(largest_prime_factor(600851475143))