# Input: Two sequences of n positive integers: price1,..., pricen and clicks1,..., clicksn.
# Output: The maximum value of price1 · c1 + ··· + pricen · cn, where c1,...,cn is a permutation
# of clicks1,..., clicksn.
# Constraints. 1 ≤ n ≤ 10^3; 0 ≤ pricei, clicksi ≤ 10^5 for all 1 ≤ i ≤ n.

from itertools import permutations

def max_dot_product(first_sequence, second_sequence):
    max_product = 0
    for permutation in permutations(second_sequence):
        dot_product = sum(first_sequence[i] * permutation[i] for i in range(len(first_sequence)))
        max_product = max(max_product, dot_product)

    return max_product

def max_dot_product_fast(first_sequence, second_sequence):
    first_sequence.sort()
    second_sequence.sort()
    return sum(list(map(lambda x: x[0] * x[1], zip(first_sequence,second_sequence))))


if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product_fast(prices, clicks))
    
