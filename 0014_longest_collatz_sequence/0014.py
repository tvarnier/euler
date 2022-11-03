def generate_sequence_length(starting):
    current = starting
    nbr_it = 0

    while current != 1:
        current = current / 2 if current % 2 == 0 else 3 * current + 1
        nbr_it = nbr_it + 1
    return nbr_it

def longest_collatz_sequence(max_starting_number):
    res = (0, 0)
    for starting in range(1, max_starting_number):
        sequence_len = generate_sequence_length(starting)
        if sequence_len > res[1]:
            res = (starting, sequence_len)
    return res[0]

if __name__ == '__main__':
    print(longest_collatz_sequence(1000000))
