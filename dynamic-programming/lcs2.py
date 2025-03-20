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


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
    