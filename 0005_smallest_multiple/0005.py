def smallest_multiple(r):
    res = r[-1]

    while 1:
        res += r[-1]
        for i in r:
            if res % i != 0:
                break
            if i == r[-1]:
                return res
            

if __name__ == '__main__':
    print(smallest_multiple(range(1, 20)))