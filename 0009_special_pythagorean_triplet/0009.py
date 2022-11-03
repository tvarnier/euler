import math

def special_pythagorean_triplet(target):
    for b in range(2, target // 2):
        for a in range(1, b - 1):
            c = math.sqrt(b ** 2 + a ** 2)
            if a + b + c == target:
                return a * b * c

if __name__ == '__main__':
    print(special_pythagorean_triplet(1000))