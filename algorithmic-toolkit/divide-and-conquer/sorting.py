from random import randint


def partition3(array, left, right):
    m1 = left
    m2 = left
    for i in range(left + 1, right + 1):
        if array[i]<= array[m2]:
            m2 += 1
            array[i], array[m2] = array[m2], array[i]
        if array[m2]< array[m1]:
            array[m2], array[m1] = array[m1], array[m2]
            m1 += 1
    return m1, m2

def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
