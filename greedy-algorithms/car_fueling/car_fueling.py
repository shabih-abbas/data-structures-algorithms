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
