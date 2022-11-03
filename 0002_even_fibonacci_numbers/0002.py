def even_fibonacci_numbers(n):
    res = 0
    last = 1
    current = 2

    while current < n:
        if current % 2 == 0:
            res += current
        
        new = current + last
        last = current
        current = new

    return res

if __name__ == '__main__':
    print(even_fibonacci_numbers(4000000))