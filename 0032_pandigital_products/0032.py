import itertools
import numpy as np

if __name__ == '__main__':
    permutations = np.array(["".join(s) for s in list(itertools.permutations("123456789"))])
    
    products = set()

    for perm in permutations:
        for multiplicand_len in range(1, 7 + 1):
            for multiplier_len in range(1, 7 + 1 - multiplicand_len):
                if int(perm[:multiplicand_len]) * int(perm[multiplicand_len:(multiplicand_len+multiplier_len)]) == int(perm[(multiplicand_len + multiplier_len):]):
                    products.add(int(perm[(multiplicand_len + multiplier_len):]))

    print(sum(products))