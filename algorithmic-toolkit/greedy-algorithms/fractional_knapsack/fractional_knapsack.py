# Input: The capacity of a backpack W as well as the weights (w1 ,...,wn) and costs (c1 ,...,cn) of n di ffrent compounds.
# Output: The maximum total value of fractions of items that fit into the backpack of the given capacity: i.e., the maximum value
# of c1 · f1 + ··· + cn · fn such that w1 ·f1 +···+wn·fn ≤ W and 0 ≤ fi ≤1 for all i (fi is the fraction of thei-th item taken to the backpack)
# Constraints. 1 ≤ n ≤ 10^3, 0 ≤ W ≤ 2 · 10^6; 0 ≤ ci ≤ 2 · 10^6, 0 < wi ≤ 2 · 10^6 for all 1 ≤ i ≤ n. All the numbers are integers.

from sys import stdin

def optimal_value(capacity, weights, values):
    if capacity<= 0: return 0
    value = 0.
    # write your code here
    index_by_dec_value_per_weight= sorted([i for i in range(len(values))],key= lambda x: values[x]/weights[x], reverse=True)
    for i in index_by_dec_value_per_weight:
        if capacity==0: return round(value,4)
        amount= min(weights[i], capacity)
        capacity-= amount
        value+= amount*values[i]/weights[i]
    return round(value,4)

if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
