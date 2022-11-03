def index_first_fibonacci_with_length(length):
    last = 1
    current = 1
    index = 2
    l = 1

    while l < length:
        index += 1
        current, last = current + last, current
        l = len(str(current))

    return index

if __name__ == '__main__':
    print(index_first_fibonacci_with_length(1000))