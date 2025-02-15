import random
import time
import timeit
def fibonacci_number(n):
    if n <= 1:
        return n

    return fibonacci_number(n - 1) + fibonacci_number(n - 2)
def fibonacci_number_fast(n):
    if n<= 1: return n
    nums= [0,1]
    for i in range(2,n+1): nums.append(nums[i-1]+nums[i-2])
    return nums[n]

if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number_fast(input_n))
