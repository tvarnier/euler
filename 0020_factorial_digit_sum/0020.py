def factorial_digit_sum(nbr):
    n = 1
    for i in range(1, nbr + 1):
        n *= i
    return sum(int(x) for x in str(n))

if __name__ == "__main__":
    print(factorial_digit_sum(100))