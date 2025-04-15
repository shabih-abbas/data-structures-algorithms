def find_seq2(f, s, seqs, r = 1, c = 1, cur_seq = []):
    found = []
    if r >= len(seqs) or c >= len(seqs[r]) or seqs[r-1][c-1] == seqs[-1][-1]: return found
    bound = len(seqs[r])
    while(r < len(seqs) and c < bound):
        j = c
        while(j < bound):
            if f[j - 1] == s[r - 1] and seqs[r][j] > seqs[r-1][j-1]:
                bound = j 
                new_seq= [*cur_seq, f[j - 1]]
                cur = find_seq2(f, s, seqs, r + 1, j + 1, new_seq)
                cur = cur if cur else [new_seq]
                found.extend(cur)
            j += 1
        r += 1
    return sorted(found, reverse= True, key= len)

def find_seq(f, s, seqs, r = 1, c = 1, cur_seq = []):
    found = []
    for i in range(r, len(seqs)):
        for j in range(c, len(seqs[i])):
            # print(i, j)
            if f[j - 1] == s[i - 1] and seqs[i][j] > seqs[i-1][j-1]:
                new_seq= [*cur_seq, f[j - 1]]
                # present= False
                # if seqs[i][j] > len(cur_seq) + 1:
                # for p in found:
                #     present = lcs2(p, new_seq) == len(new_seq)
                #     if present: break
                
                # if not present:
                    # print(cur_seq)
                cur = find_seq(f, s, seqs, i + 1, j + 1, new_seq)
                    # print(cur)
                cur = cur if cur else [new_seq]
                # if found:
                #     for new in range(len(cur)-1, -1, -1):
                #         if lcs2(found[-1], cur[new]) == len(cur[new]): del cur[new]
                # if cur:
                found.extend(cur)
    found.sort(reverse= True, key= len)
    for f_seq in range(len(found) -1, -1, -1):
        for s_seq in range(f_seq):
            if lcs2(found[f_seq], found[s_seq]) == len(found[f_seq]):
                del found[f_seq]
                break
    return found

def lcs2(first_sequence, second_sequence):
    if not(first_sequence and second_sequence): return 0
    n = len(first_sequence)
    m = len(second_sequence)
    seq= [0]* (n + 1)
    # print(seq)
    for i in range(1, m + 1):
        cur = [0]
        for j in range(1, n + 1):
            u = seq[j]
            l = cur[j - 1]
            ul = seq[j - 1]
            if first_sequence[j - 1] == second_sequence[i - 1] and u == l and u == ul: 
                cur.append(u + 1)
                # print(first_sequence[j - 1], j, second_sequence[i - 1], i, seq[i][j])
                if cur[j] == n or cur[j] == m: return cur[j] # helps in find_seq
            else: 
                cur.append(max(u, l))
                # print(first_sequence[j - 1], j, second_sequence[i - 1], i, seq[i][j])
            
        seq = cur[:]
        # print(seq)
    return seq[n]

def lcs3(first_sequence, second_sequence, third_sequence, fast= True):
    if not(first_sequence and second_sequence and third_sequence): return 0
    f_len = len(first_sequence)
    s_len = len(second_sequence)
    lcs = 0
    seq= [[0]* (f_len + 1)]
    for i in range(1, s_len + 1):
        cur = [0]
        for j in range(1, f_len + 1):
            u = seq[i - 1][j]
            l = cur[j - 1]
            ul = seq[i - 1][j - 1]
            
            if first_sequence[j - 1] == second_sequence[i - 1] and u == l and u == ul: 
                cur.append(u + 1)
                
            else: 
                cur.append(max(u, l))
                
        seq.append(cur[:])

    if not seq[s_len][f_len]: return 0
    
    f_seq_s= find_seq2(first_sequence, second_sequence, seq) if fast else find_seq(first_sequence, second_sequence, seq)
    print(f_seq_s)
    for s in f_seq_s:
        if lcs >= len(s): return lcs
        lcs = max(lcs, lcs2(s, third_sequence))
            
    return lcs
def lcs3_w(nums):
    if len(nums) < 3: return 0
    return lcs3(nums[:len(nums)//3], nums[len(nums)//3 : 2 * len(nums)//3], nums[2 * len(nums)//3:])

def lcs3_slow_w(nums):
    if len(nums) < 3: return 0
    return lcs3(nums[:len(nums)//3], nums[len(nums)//3 : 2 * len(nums)//3], nums[2 * len(nums)//3:], False)

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
    
