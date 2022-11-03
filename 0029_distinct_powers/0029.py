def distinct_powers(a_limit, b_limit):
    unique_powers = set()

    for a in range(a_limit[0], a_limit[1] + 1):
        for b in range(b_limit[0], b_limit[1] + 1):
            unique_powers.add(a**b)
    return len(unique_powers)

if __name__ == "__main__":
    print(distinct_powers((2, 100), (2, 100)))