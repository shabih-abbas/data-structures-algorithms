# python3
def shift_down(array, i):
    swaps = []
    n = len(array)
    if i < len(array):
        subs = i
        left_chlid = i * 2 + 1
        right_chlid = i * 2 + 2
        if left_chlid < n and array[subs] > array[left_chlid] : subs = left_chlid
        if right_chlid < n and array[subs] > array[right_chlid] : subs = right_chlid
        if subs != i:
            swaps.append((i, subs))
            array[i], array[subs] = array[subs], array[i]
            swaps.extend(shift_down(array, subs))
    return swaps
def build_heap(data):
    swaps = []
    for i in range(len(data)//2 - 1, -1, -1):
        swaps.extend(shift_down(data, i))
    return swaps

def build_heap_selection(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
