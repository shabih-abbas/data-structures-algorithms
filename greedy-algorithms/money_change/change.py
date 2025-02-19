def change_brute_force(money):
    coins=[1,5,10]
    if money == 0:
        return 0  
    if money < 0:
        return float('inf')  

    min_coins = float('inf')
    for coin in coins:
        res = change_brute_force(money - coin)
        if res != float('inf'):
            min_coins = min(min_coins, res + 1)

    return min_coins
def change(money):
    # write your code here

    return (money//10)+((money%10)//5)+(money%5)


if __name__ == '__main__':
    m = int(input())
    print(change_brute_force(m))
