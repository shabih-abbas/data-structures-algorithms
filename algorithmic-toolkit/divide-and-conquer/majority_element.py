from binary_search_duplicates import binary_search_dup as first_instance

def majority_element_naive(elements):
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0

def majority_element_sort(elements):
    len_elements= len(elements)
    if not elements: return 0
    if len_elements==1: return 1
    if len_elements==2: return elements[0]==elements[1]
    elements.sort()
    m = first_instance(elements, elements[len_elements // 2])
    return int(elements[m]==elements[m + len_elements // 2]) if len_elements - m > len_elements//2 else 0
    
def majority_element_fast(elements):
    len_elements= len(elements)
    if not len_elements: return 0
    if len_elements==1: return 1
    if len_elements==2: return elements[0]==elements[1]
    pairs = {elements[i] for i in range(len_elements) if (len_elements > i + 1 and elements[i]==elements[i + 1]) or (len_elements > i + 2 and elements[i]==elements[i + 2])}
    for pair in pairs:
        if elements.count(pair) > len_elements / 2: return 1
    return 0

# The last one is similar to the first except that it reduces the no. of operations by atleast a factor of 2, 
# but the time complexity is still O(n^2). However the middle one is bounded by O(nlogn) and is the fastest of the three.

if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element_fast(input_elements))
