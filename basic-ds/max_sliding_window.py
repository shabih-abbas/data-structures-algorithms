# python3
from stack_with_max_naive import StackWithMax

class Queue():
    def __init__(self):
        self.incoming = StackWithMax()
        self.outgoing = StackWithMax()
    def enqueue(self, a):
        self.incoming.Push(a)
    def dequeue(self):
        if not self.outgoing.isEmpty(): return self.outgoing.Pop()
        while not self.incoming.isEmpty(): self.outgoing.Push(self.incoming.Pop())
        return self.outgoing.Pop()
    def max_in_queue(self): 
        assert(not(self.incoming.isEmpty() and self.outgoing.isEmpty()))
        if self.incoming.isEmpty(): return self.outgoing.Max()
        if self.outgoing.isEmpty(): return self.incoming.Max()
        return max(self.outgoing.Max(), self.incoming.Max())

def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))

    return maximums
def max_sliding_window(sequence, m):
    
    maximums = []
    if(len(sequence) >= m):
        queue = Queue()
        for i in range(m): queue.enqueue(sequence[i])
        maximums.append(queue.max_in_queue())
        for i in range(m, len(sequence)):
            queue.dequeue()
            queue.enqueue(sequence[i])
            maximums.append(queue.max_in_queue())
    return maximums



if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window(input_sequence, window_size))

