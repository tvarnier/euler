import itertools

if __name__ == '__main__':
    print(''.join( list(itertools.permutations("0123456789"))[999999] ))