from collections import deque

def compute_operations_greedy(n):
    interim = deque([n])
    while interim[0] > 1 :
        if interim[0] % 3 == 0: interim.appendleft(interim[0]/3)
        elif interim[0] % 2 == 0: interim.appendleft(interim[0]/2)
        else : interim.appendleft(interim[0] - 1)

    return list(map(int, interim))

def compute_operations(n):
    interim = deque([n])
    steps = [0]
    for n in range(2, n + 1):
        min_steps = n
        if n / 3 > 0: min_steps= min(min_steps, steps[n - 3 * (n / 3)] + 1)
        if n / 2 > 0: min_steps= min(min_steps, steps[n - 2 * (n / 2)] + 1)
        min_steps= min(min_steps, steps[n - 1] + 1)
        steps.append(min_steps)
    while(n > 1):
        if 




if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
