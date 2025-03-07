from itertools import combinations

def inversions_and_sort(a):
    if len(a) < 2: return 0, a 
    cur_inver= 0
    a_sorted=[]
    m = len(a)//2
    inver_first_half, first= inversions_and_sort(a[:m])
    inver_sec_half, second= inversions_and_sort(a[m:])
    f, s = 0, 0
    while f < len(first) and s < len(second):
        if first[f] > second[s]:
            cur_inver += 1
            a_sorted.append(second[s])
            s += 1
        else: 
            a_sorted.append(first[f])
            f += 1
            if f < len(first): cur_inver += s
    if f < len(first):
        cur_inver += (len(first) - f - 1) * s
        for reminaing in first[f:]: a_sorted.append(reminaing)
    else: 
        for reminaing in second[s:]: a_sorted.append(reminaing)
    return cur_inver + inver_first_half + inver_sec_half, a_sorted

def inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions

def inversions(a):
    inver, a= inversions_and_sort(a)
    return inver



if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(inversions(elements))
