import array

def prime_from_index(index):
    if index < 1:
        return 0

    primes = array.array('L', [2])
    
    count = index - 1
    num = 3
    while count != 0:
        for p in primes:
            if p * 3 > num:
                primes.append(num)
                # print(num)
                count -= 1
                break
            if (num % p) == 0:
                break
        num += 2

    return primes[index - 1]


if __name__ == '__main__':
    print(prime_from_index(10001))