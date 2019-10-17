# python3

from collections import namedtuple, deque
import heapq

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs(n_workers, jobs):
    result = []
    worker_heap = []
    for i in range(n_workers):
        heapq.heappush(worker_heap, [0, i])

    jobs_queue = deque([])
    for job in jobs:
        jobs_queue.append(job)

    while len(jobs_queue) > 0:
        current_job = jobs_queue.popleft()
        smallest_worker = heapq.heappop(worker_heap)
        result.append(AssignedJob(smallest_worker[1], smallest_worker[0]))
        smallest_worker[0] += current_job
        heapq.heappush(worker_heap, smallest_worker)

    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
