def lcs2_brute(first_sequence, second_sequence):
    max_seq = 0
    f = 0
    while f < len(first_sequence) and len(first_sequence) - f > max_seq:
        s = 0
        while(s < len(second_sequence) and first_sequence[f]!=second_sequence[s]) : s += 1
        if s < len(second_sequence):
            s += 1
            max_seq = max(max_seq, 1)
            for r in range(f + 1, len(first_sequence)): max_seq = max(max_seq, lcs2_brute(first_sequence[r:], second_sequence[s:]) + 1)
        f+=1
    return max_seq
def lcs2_brute_w(array):
    if len(array) < 2: return 0
    return lcs2_brute(array[:len(array)//2], array[len(array)//2:])

def lcs2(first_sequence, second_sequence):
    n = len(first_sequence)
    m = len(second_sequence)
    seq= [[0]* (n + 1)]* (m + 1)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            u = seq[i-1][j]
            l = seq[i][j-1]
            if first_sequence[j - 1] == second_sequence[i - 1] and u == l: seq[i][j]= u + 1
            else: seq[i][j] = max(u, l)
    return seq[m][n]
def lcs2_w(array):
    if len(array) < 2: return 0
    return lcs2(array[:len(array)//2], array[len(array)//2:])


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
    