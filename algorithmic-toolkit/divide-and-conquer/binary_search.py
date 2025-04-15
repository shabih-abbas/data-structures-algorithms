import math

def binary_search(keys, query, index=0):
    if not keys: return -1
    if query < keys[0] or query > keys[-1]: return -1
    m = math.ceil(len(keys)/2)-1
    if query == keys[m]: return m + index
    if query < keys[m]: return binary_search(keys[:m], query, index)
    if query > keys[m]: return binary_search(keys[m+1:], query, index+m+1)

def binary_search_i(keys, query):
    if not keys: return -1
    upper = len(keys)-1
    lower = 0
    if query < keys[lower] or query > keys[upper]: return -1
    while(not upper < lower):
        m = lower + (upper - lower) // 2
        if keys[m] == query: return m
        if query > keys[m]: lower= m + 1
        else: upper = m - 1
    return -1

if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search_i(input_keys, q), end=' ')
