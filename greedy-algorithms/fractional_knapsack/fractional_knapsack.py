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
