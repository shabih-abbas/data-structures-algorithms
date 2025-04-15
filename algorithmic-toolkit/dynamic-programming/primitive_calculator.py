from collections import deque

def compute_operations_greedy(n):
    interim = deque([n])
    while interim[0] > 1 :
        if interim[0] % 3 == 0: interim.appendleft(interim[0]/3)
        elif interim[0] % 2 == 0: interim.appendleft(interim[0]/2)
        else : interim.appendleft(interim[0] - 1)

    return list(map(int, interim))

def compute_operations_d(n):
    interim= deque([n])
    steps = [-1] * (n + 1)
    for i in range(1, n + 1):
        if steps[i] < 1 : steps[i] = steps[i-1] + 1
        else : steps[i] = min(steps[i], steps[i-1] + 1)
        if not i * 2 > n: 
            if steps[i * 2] < 1: steps[i * 2]= steps[i] + 1
            else: steps[i * 2]= min(steps[i * 2], steps[i] + 1)
        if not i * 3 > n: 
            if steps[i * 3] < 1: steps[i * 3]= steps[i] + 1
            else: steps[i * 3]= min(steps[i * 3], steps[i] + 1)
    while(not n < 1):
        if n % 3 == 0 and steps[n // 3] == steps[n] - 1: 
            n = n // 3
        elif n % 2 == 0 and steps[n // 2] == steps[n] - 1: 
            n = n // 2
        else: 
            n -= 1
        interim.appendleft(n)    
    return list(interim)[1:]

if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations_d(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
    