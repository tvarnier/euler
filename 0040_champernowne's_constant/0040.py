if __name__ == '__main__':
    sum = 1
    
    div = 10
    len = 1

    count = 0
    next = 1

    i = 0
    while next <= 1000000:
        i += 1
        if i // div > 0:
            len += 1
            div *= 10
        if count + len >= next:
            sum *= int(str(i)[next - count - 1])
            next *= 10
        count += len 
    print(sum)