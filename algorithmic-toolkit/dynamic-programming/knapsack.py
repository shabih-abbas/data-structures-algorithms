from sys import stdin

def maximum_gold_brute(capacity, weights):
    p_sets= [[]]
    for w in weights:
        sets = [s + [w] for s in p_sets]
        p_sets.extend(sets)
    return max([sum(s) for s in p_sets if sum(s) <= capacity])


def maximum_gold(capacity, weights, gold_dict= None):
    # print(gold_dict)
    if not(capacity and weights): return 0
    if gold_dict == None: gold_dict = {}
    # if capacity in weights: return capacity
    max_gold = gold_dict.get((capacity, len(weights)),-1)
    if max_gold != -1: return max_gold
    max_gold = maximum_gold(capacity, weights[:len(weights)-1], gold_dict)
    # if max_gold == capacity: return max_gold
    if weights[-1] <= capacity:
        max_gold = max(max_gold, maximum_gold(capacity - weights[-1], weights[:len(weights) - 1], gold_dict) + weights[-1])
    gold_dict[(capacity, len(weights))] = max_gold
    
    return max_gold
def maximum_gold_w(weights):
    if not weights: return 0
    capacity= 10000
    res = maximum_gold(capacity, weights, {})
    # print(f"capacity: {capacity}, max: {res}")
    return res
def maximum_gold_brute_w(weights):
    if not weights: return 0
    capacity= 10000
    res = maximum_gold_brute(capacity, weights)
    # print(f"[brute] capacity: {capacity}, max: {res}")
    return res

if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
    