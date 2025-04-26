# python3

from collections import namedtuple

class WorkersQ():
    def __init__(self, n):
        self.size = n
        self.q = list(zip(range(n), [0] * n))
    def shift_down(self, i):
        if i < self.size:
            subs = i
            left_chlid = i * 2 + 1
            right_chlid = i * 2 + 2
            
            if left_chlid < self.size:
                if self.q[subs][1] > self.q[left_chlid][1] or (self.q[subs][1] == self.q[left_chlid][1] and self.q[subs][0] > self.q[left_chlid][0]): subs = left_chlid
            if right_chlid < self.size:
                if self.q[subs][1] > self.q[right_chlid][1] or (self.q[subs][1] == self.q[right_chlid][1] and self.q[subs][0] > self.q[right_chlid][0]): subs = right_chlid
            if subs != i:
                self.q[i], self.q[subs] = self.q[subs], self.q[i]
                self.shift_down(subs)
    def top_worker(self):
        assert(self.size)
        return self.q[0]
    def assign_job(self, job):
        assert(self.size)
        self.q[0] = (self.q[0][0], self.q[0][1] + job)
        self.shift_down(0)

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

def assign_jobs_fast(workers, jobs):
    result = []
    if workers:
        queue = WorkersQ(workers)
        for job in jobs:
            worker = queue.top_worker()
            result.append(AssignedJob(worker[0], worker[1]))
            queue.assign_job(job)
    return result

def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = [0] * n_workers
    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job

    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs_fast(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
