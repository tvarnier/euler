import math

if __name__ == '__main__':
    abundants = []
    for i in range(12, 28123):
        if i % 2 == 0 or i % 5 == 0:
            if i < sum([div for div in range(1, (i // 2) + 1) if not i % div]):
                abundants.append(i)
    
    l = len(abundants)

    sum_abundants = set()
    i = 0
    while i < l:
        j = i
        while j < l and abundants[i] + abundants[j] < 28123:
            sum_abundants.add(abundants[i] + abundants[j])
            j += 1
        i += 1
    
    res = 0
    for i in range(1, 28123):
        if i not in sum_abundants:
            res += i
    print(res)