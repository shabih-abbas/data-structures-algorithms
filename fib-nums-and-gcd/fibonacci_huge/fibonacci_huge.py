def fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m
def fibonacci_huge_fast(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current

def fibonacci_huge_faster(n, m):
    if n <= 1:
        return n
    nums=[0,1]
    cycle  =  0
    
    for i in range(2,n + 1):
        nums.append((nums[i-1]+nums[i-2]) % m)
        if len(nums)%2==0 and nums[:len(nums)//2]==nums[len(nums)//2:]:
            cycle = len(nums)//2
            break
    if cycle > 0: return nums[n % cycle]
    
    return nums[n]


if __name__ == '__main__':
    # n, m = map(int, input().split())
    # print(fibonacci_huge_naive(n, m))
    print(fibonacci_huge_faster(6,6))
