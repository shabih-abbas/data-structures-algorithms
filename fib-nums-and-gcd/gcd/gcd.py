def gcd(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd
def gcd_fast(a,b):
    d= max(a,b)
    r= min(a,b)
    while(d % r != 0):
        d, r = r, d % r
    return r


if __name__ == "__main__":
    # a, b = map(int, input().split())
    # print(gcd(a, b))
    print(gcd_fast(28851538,1183019))
