# Input: An integer n.
# Output: The last digit of F0^2 +F1^2 +··· + Fn^2
# Constraints. 0 ≤ n ≤ 10^14; time limit: 5sec; memory limit: 512MB

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"../")))
from fibonacci_huge.fibonacci_huge import fibonacci_huge_faster as fibonacci_modulo

def fibonacci_sum_squares(n):
    if n <= 1:
        return n

    previous, current, sum = 0, 1, 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

def fibonacci_sum_squares_fast(n):
    if n <= 1: return n
    return (fibonacci_modulo(n,10)*fibonacci_modulo(n+1,10))%10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares_fast(n))
    
