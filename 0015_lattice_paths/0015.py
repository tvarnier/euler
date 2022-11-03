import math

def lattice_paths(len):
    return (math.factorial(len * 2) / (math.factorial(len) ** 2))  

if __name__ == '__main__':
    print(lattice_paths(20))