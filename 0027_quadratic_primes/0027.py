import math

def is_prime(n):
    n = abs(n)
    for i in range(2,int(math.sqrt(n))+1):
        if (n%i) == 0:
            return False
    return True

if __name__ == '__main__':
    max = (0, 0, 0)

    for a in range (-999, 1000):
        for b in range(0, 1001):
            # b must be a prime to get a prime with n = 0, n^2 + an + b = b 
            if is_prime(b):
                count = 0
                n = 0
                while is_prime(n**2 + a * n + b):
                    count += 1
                    n += 1
                if count > max[2]:
                    max = (a, b, count)
    print(max)
    print(max[0] * max[1])
