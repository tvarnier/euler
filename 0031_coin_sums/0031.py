coin = [1, 2, 5, 10, 20, 50, 100, 200]

def coin_sums(index, amount):
    sum = 0
    if amount > 200:
        return 0
    elif amount == 200:
        return 1
    for i in range(index, len(coin)):
        sum += coin_sums(i, amount + coin[i])
    return sum

if __name__ == '__main__':
    print(coin_sums(0, 0))