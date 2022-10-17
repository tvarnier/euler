"""
https://projecteuler.net/problem=14

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

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
