from binary_search import binary_search_i as binary_search
def binary_search_dup(keys, query):
    if not keys : return -1
    index= binary_search(keys, query)
    prev_index=-1
    while(not index < 1):
        prev_index= binary_search(keys[:index],query)
        if prev_index==-1: break
        index= prev_index
    return index
# The above is not efficient as it starts from the begining of the list everytime and does not inherit the lower bounds of the previous searches.
def binary_search_dup_i(keys, query):
    if not keys: return -1
    upper = len(keys)-1
    lower = 0
    index = []
    if query < keys[lower] or query > keys[upper]: return -1
    while(not (upper < lower or query > keys[upper])):
        m = lower + (upper - lower) // 2
        if keys[m] == query: 
            index.append(m)
            upper = m - 1
        if query > keys[m]: lower= m + 1
        else: upper = m - 1
    return index[-1] if index else -1

if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search_dup_i(input_keys, q), end=' ')
