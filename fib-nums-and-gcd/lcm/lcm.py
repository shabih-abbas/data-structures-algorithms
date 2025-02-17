import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from gcd.gcd import gcd_fast
def lcm(a, b):
    for l in range(1, a * b + 1):
        if l % a == 0 and l % b == 0:
            return l

    assert False
def lcm_fast(a, b):
    return int(a * b / gcd_fast(a, b))

if __name__ == '__main__':
    # a, b = map(int, input().split())
    # print(lcm(a, b))
    print(lcm_fast(761457,614573))
    