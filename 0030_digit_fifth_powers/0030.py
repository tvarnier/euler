def get_limit(exp):
    i = 0
    sum = 0
    while i < len(str(sum)):
        sum += (9 ** exp)
        i += 1
    return sum

def get_sum(n, exp):
    sum = 0
    while (n != 0):
        sum += ((n % 10) ** exp)
        n = n // 10
    return sum

def sum_digits_exp(exp):
    sum = 0
    
    for i in range(2, get_limit(exp)):
        if i == get_sum(i, exp):
            sum += i
    return sum

if __name__ == '__main__':
    print(sum_digits_exp(5))