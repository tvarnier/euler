def containsAll(str, set):
    return 0 not in [c in str for c in set]

if __name__ == '__main__':
    max = (0, 0)
    for nbr in range(1, 9876):
        s = ""
        i = 1
        while len(s) < 9:
            s = s + str(nbr * i)
            i += 1

        if len(s) == 9 and containsAll(s, "123456789"):
            if int(s) > max[1]:
                print(nbr, int(s))
                max = (nbr, int(s))

    print("MAX : ", max)