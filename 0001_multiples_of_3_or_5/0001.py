if __name__ == '__main__':
    res = 0
    
    for i in range(0, 1000):
        if i % 3 == 0 or i % 5 == 0:
            res += i
    
    print(res)
