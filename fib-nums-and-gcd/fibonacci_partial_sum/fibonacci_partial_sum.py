# Input: Integers m ≤ n.
# Output: The last digit of Fm + Fm+1 + ··· + Fn
# Constraints. 0 ≤ m ≤ n ≤ 10^14; time limit: 5sec; memory limit: 512MB

# Uses python3
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"../")))
from fibonacci_sum_last_digit.fibonacci_sum_last_digit import fibonacci_sum_faster

def fibonacci_partial_sum_naive(from_, to):
    _sum = 0
    current = 0
    _next  = 1

    for i in range(to + 1):
        if i >= from_:
            _sum += current

        current, _next = _next, current + _next

    return _sum % 10

def fibonacci_partial_sum_fast(from_, to):
    if from_ > to: raise ValueError('Please Enter a correct range')
    if from_ < 2: return fibonacci_sum_faster(to)
    return (fibonacci_sum_faster(to)-fibonacci_sum_faster(from_-1)+10)%10


if __name__ == '__main__':
    input = sys.stdin.read()
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_fast(from_, to))
    
