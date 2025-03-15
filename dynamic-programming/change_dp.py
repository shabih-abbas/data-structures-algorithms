def change(money):
    if not money: return 0
    coins = [0]
    denom = [1, 3, 4]
    for m in range(1, money + 1):
        min_coins = m
        for d in denom:
            if not m - d < 0: min_coins = min(min_coins, coins[m - d] + 1)
        coins.append(min_coins)
    return coins[money]


if __name__ == '__main__':
    m = int(input())
    print(change(m))
