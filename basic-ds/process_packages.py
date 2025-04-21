# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])

class Deque():
    def __init__(self, size):
        self.queue = [None] * (size + 1)
        self.front = 0
        self.tail = 0
    def enqueue(self, a):
        assert((self.tail + 1) % len(self.queue) != self.front)
        self.queue[self.tail] = a 
        self.tail = (self.tail + 1) % len(self.queue)
    def dequeue(self):
        assert(self.front != self.tail)
        self.front = (self.front + 1) % len(self.queue)
    def top_front(self):
        assert(self.front != self.tail)
        return self.queue[self.front]
    def top_back(self):
        assert(self.front != self.tail)
        return self.queue[(self.tail - 1 + len(self.queue)) % len(self.queue)]
    def is_empty(self):
        return self.front == self.tail
    def is_full(self):
        return (self.tail + 1) % len(self.queue) == self.front



class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = Deque(size)
        

    def process(self, request):
        
        if self.finish_time.is_empty() or request.arrived_at >= self.finish_time.top_back():
            self.finish_time = Deque(self.size)
            self.finish_time.enqueue(request.arrived_at + request.time_to_process) 
            return Response(False, request.arrived_at)
        while(request.arrived_at >= self.finish_time.top_front()): self.finish_time.dequeue()
        if self.finish_time.is_full(): return Response(True, -1)
        started_at = self.finish_time.top_back()
        self.finish_time.enqueue(started_at +  + request.time_to_process)
        return Response(False, started_at)


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
