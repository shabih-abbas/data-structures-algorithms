# import sys
# sys.path.append("../fibonacci_huge")
# from fibonacci_huge import fibonacci_huge_faster as fibonacci_modulo
def fibonacci_modulo(n, m):
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

def fibonacci_sum(n):
    if n <= 1:
        return n

    previous, current, _sum = 0, 1, 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        _sum += current

    return _sum % 10

def fibonacci_sum_fast(n):
    if n <= 1:
        return n

    previous, current, _sum = 0, 1, 1

    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10
        _sum = (_sum + current) % 10

    return _sum

def fibonacci_sum_faster(n):
    if n <= 1:
        return n
    return ((fibonacci_modulo(n+2,10)-1)+10)%10

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_faster(n))
    
