# Input: Integers d and m, as well as a sequence of integers stop1 < stop2 < ··· < stopn.
# Output: The minimum number of refils to get from one city to another if a car can travel
# at most m miles on a full tank. The distance between the cities is d miles and there are gas stations
# at distances stop1, stop2,..., stopn along the way. We assume that a car starts with a full tank.
# Constraints. 1 ≤ d ≤ 10^5. 1 ≤ m ≤ 400. 1 ≤ n ≤ 300. 0 < stop1 < stop2 < ··· < stopn < d.

from sys import stdin

def min_refills(distance, tank, stops):
    # write your code here
    if distance<= tank: return 0
    stop=0
    stop_count=0
    for i in range(len(stops)):
        if distance - stop <= tank: return stop_count
        if stops[i] - stop > tank: return -1
        if i < len(stops)-1 and stops[i+1] - stop <= tank: continue
        stop= stops[i]
        stop_count+=1
        
    return -1 if distance - stop > tank else stop_count


if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
