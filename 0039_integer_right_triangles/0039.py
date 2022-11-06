if __name__ == '__main__':
    max = (0, 0)
    for perimeter in range (1, 1001):
        count = 0
        for a in range(1, perimeter // 3):
            # a^2 + b^2 = c^2
            # p = a + b +c
            #
            # => a^2 + b^2 = (p - a - b)^2
            #    a^2 + b^2 = p^2 + a^2 + b^2 - 2pa - 2pb + 2ab
            #            0 = p^2 - 2pa - 2pb + 2ab
            #    2pb - 2ab = p^2 - 2pa
            #   b(2p - 2a) = p^2 - 2pa
            #            b = (p^2 - 2pa) / (2p - 2a)
            b = (perimeter ** 2 - 2*perimeter*a) // (2*perimeter - 2*a)
            if (a**2 + b**2) == (perimeter - a - b) ** 2:
                count += 1
                # print(perimeter, a, b, perimeter - a -b)
        if count > max[1]:
            max = (perimeter, count)
    print(max)

