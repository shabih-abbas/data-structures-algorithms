# Input: A positive integer n.
# Output: The maximum k such that n can be represented as the
# sum a1 + ··· + ak of k distinct positive integers.
# Constraints. 1 ≤ n ≤ 10^9

def optimal_summands(n):
    summands = []
    rest = n
    i = 1
    while not rest - i <= i:
        summands.append(i)
        rest-=i
        i += 1
    # for i in range(1,n//2+1):
    #     if rest == i: 
    #         summands.append(i)
    #         return summands
    #     if rest - i > i:
    #         summands.append(i)
    #         rest -= i
    #     else : break
    summands.append(rest)
    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
