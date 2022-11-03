import math

def highly_divisible_triangular_number(nbr_divisors_target):
    triangle_number = 0
    i = 1
    while 1:
        triangle_number = triangle_number + i
        nbr_factor = sum(2 for div in range(1, round(math.sqrt(triangle_number) + 1)) if not triangle_number % div)
        if nbr_factor > nbr_divisors_target:
            return triangle_number
        i = i + 1

if __name__ == '__main__':
    print(highly_divisible_triangular_number(500))
