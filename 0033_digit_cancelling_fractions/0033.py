def reduct_fraction(dividend, denominator):
    div = dividend if dividend < denominator else denominator
    while div > 1:
        if dividend % div == 0 and denominator % div == 0:
            dividend = dividend // div
            denominator = denominator // div
            div = dividend if dividend < denominator else denominator
        else:
            div -= 1
    return (dividend, denominator)
    
if __name__ == '__main__':
    product_dividend = 1
    product_denominator = 1

    for x in range(10, 100):
        for y in range(x + 1, 100):
            if x != y:
                if x // 10 == y // 10 and y % 10 != 0:
                    if x / y == (x % 10) / (y % 10):
                        print(x, y)
                        product_dividend *= x
                        product_denominator *= y
                if x // 10 == y % 10 and y // 10 != 0 and y % 10 != 0:
                    if x / y == (x % 10) / (y // 10):
                        print(x, y)
                        product_dividend *= x
                        product_denominator *= y
                if x % 10 == y // 10 and y % 10 != 0:
                    if x / y == (x // 10) / (y % 10):
                        print(x, y)
                        product_dividend *= x
                        product_denominator *= y
                if x % 10 == y % 10 and y // 10 != 0 and y % 10 != 0:
                    if x / y == (x // 10) / (y // 10):
                        print(x, y)
                        product_dividend *= x
                        product_denominator *= y

    print("Product : ", product_dividend, product_denominator)
    print("Product : ", reduct_fraction(product_dividend, product_denominator))