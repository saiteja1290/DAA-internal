class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

def job_sequencing(jobs):
    jobs.sort(key=lambda x: x.profit, reverse=True)

    n = len(jobs)
    result = [-1] * n  # To store the result
    max_deadline = max(job.deadline for job in jobs)
    print(max_deadline)

    # Iterate through each job
    for i in range(n):
        for j in range(min(max_deadline, jobs[i].deadline) - 1, -1, -1):
            if result[j] == -1:
                result[j] = jobs[i].id
                break
    print(result)
    scheduled_jobs = []
    for i in result:
        if i != -1:
            scheduled_jobs.append(i)
    

    return scheduled_jobs
if __name__ == "__main__":
    jobs = [
        Job(1, 2, 100),
        Job(2, 1, 19),
        Job(3, 2, 27),
        Job(4, 1, 25),
        Job(5, 3, 15)
    ]

    scheduled_jobs = job_sequencing(jobs)
    print("Scheduled Jobs:", scheduled_jobs)
