# Input: A sequence of positive integers.
# Output: The largest integer that can be obtained by concatenating
# the given integers in some order.
# Constraints. 1 ≤ n ≤ 100; 1 ≤ ai ≤ 10^3 for all 1 ≤ i ≤ n.

from itertools import permutations
LARGEST_LEN = 4
def comparison(x):
    len_x = len(x)
    chars_to_add = LARGEST_LEN - len_x 
    for i in range(chars_to_add): x+= x[i % len_x]
    return int(x)
def largest_number_naive(numbers):
    if not numbers: return 0
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest
def largest_number_fast(numbers):
    if not numbers: return 0
    numbers = list(map(str, numbers))
    numbers.sort(key= comparison, reverse=True)
    return int("".join(numbers))


if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number_fast(input_numbers))
