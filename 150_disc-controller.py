import heapq

def solution(jobs):
    # Step 1: add job index to each job so we can apply tie-breaking by index
    jobs = [(s, l, i) for i, (s, l) in enumerate(jobs)]
    # Sort jobs by request time first (because we process arrivals in order)
    jobs.sort(key=lambda x: x[0])

    n = len(jobs)  # total number of jobs
    time = 0       # current time
    idx = 0        # pointer to jobs list
    total_turnaround = 0  # sum of turnaround times
    pq = []        # priority queue: (duration, request_time, job_id)

    while idx < n or pq:
        # Step 2: push all jobs that have arrived into the heap
        while idx < n and jobs[idx][0] <= time:
            s, l, i = jobs[idx]
            heapq.heappush(pq, (l, s, i))  # priority: shortest duration, then earliest request, then smallest index
            idx += 1

        if pq:
            # Step 3: pick the job with highest priority (min-heap does the ordering)
            l, s, i = heapq.heappop(pq)
            time += l  # disk works for 'l' ms
            turnaround = time - s  # turnaround = finish time - request time
            total_turnaround += turnaround
        else:
            # No job available yet, jump time forward to the next job's request
            time = jobs[idx][0]

    # Step 4: return integer part of average turnaround time
    return total_turnaround // n

print(solution([[0, 3], [1, 9], [3, 5]]))  # Expected output: 8