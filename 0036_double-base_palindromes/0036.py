import math

def is_palindrome(n):
    if n < 10:
        return True
    
    digits = int(math.log10(n))+1
    
    div1 = 10 ** digits
    div2 = 10

    while div1 > div2:
        if (n % div1) // (div1 / 10) != (n % div2) // (div2 / 10):
            return False
        div1 /= 10
        div2 *= 10
    
    return True

def is_palindrome_binary(n):
    if n < 2:
        return True
    
    digits = int(math.log2(n))+1
    
    div1 = 2 ** digits
    div2 = 2

    while div1 > div2:
        if (n % div1) // (div1 / 2) != (n % div2) // (div2 / 2):
            return False
        div1 /= 2
        div2 *= 2
    
    return True

if __name__ == '__main__':
    sum_palindromes = 0
    for i in range(1, 1000000):
        if is_palindrome(i) and is_palindrome_binary(i):
            print(i, bin(i))
            sum_palindromes += i

    print(sum_palindromes)