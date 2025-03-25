def find_seq(f, s, seqs, r = 1, c = 1, pos = 1):
    found = []
    for i in range(r, len(seqs)):
        for j in range(c, len(seqs[i])):
            if seqs[i][j] == pos and pos > seq[i-1][j] and pos > seq[i][j-1]:
                cur = find_seq(f, s, seqs, r + 1, c + 1, pos + 1)
                if cur:
                    cur = [[f[j - 1]] + c for c in cur]
                else: cur = [[f[j - 1]]]
            found = found + cur
    return found
    
def lcs3(first_sequence, second_sequence, third_sequence):
    if not(first_sequence and second_sequence and third_sequence): return 0
    f_len = len(first_sequence)
    s_len = len(second_sequence)
    t_len = len(third_sequence)
    f_seq_s= []
    seq= [[0]* (f_len + 1)]
    for i in range(1, s_len + 1):
        cur = [0]
        for j in range(1, f_len + 1):
            u = seq[i - 1][j]
            l = cur[j - 1]
            ul = seq[i - 1][j - 1]
            if first_sequence[j - 1] == second_sequence[i - 1] and u == l and u == ul: 
                cur.append(u + 1)
                # print(first_sequence[j - 1], j, second_sequence[i - 1], i, seq[i][j])
            else: 
                cur.append(max(u, l))
                # print(first_sequence[j - 1], j, second_sequence[i - 1], i, seq[i][j])
        seq.append(cur[:])
    for i in range(1, s_len + 1):
        for j in range(1, f_len + 1):
            u = seq[i - 1][j]
            l = seq[i][j - 1]
            
    return seq[n]

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))
