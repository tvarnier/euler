def repetend_length(denominator):
    k = 0

    while (10 ** k) % denominator != 1 or k == 0:
        k += 1

    return k

if __name__ == '__main__':
    max_repetend = (0, 0)
    for denominator in range (2, 1000):
        if denominator % 2 != 0 and denominator % 5 != 0:
            length = repetend_length(denominator)
            if length > max_repetend[1]:
                max_repetend = (denominator, length)

    print(max_repetend)
