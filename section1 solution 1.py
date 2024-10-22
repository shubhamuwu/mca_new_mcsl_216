# Defining the jobs and their respective service times
jobs = [1, 5, 2, 10]
service_times = [3, 7, 4, 8]

# Creating a list of tuples (job, service_time)
job_service_pairs = list(zip(jobs, service_times))

# Sorting based on service time
sorted_jobs = sorted(job_service_pairs, key=lambda x: x[1])

# Calculating the total time spent in the system
waiting_time = 0
total_time = 0
waiting_times = []

# Calculating waiting time for each job
for job, service_time in sorted_jobs:
    waiting_times.append(waiting_time)
    total_time += waiting_time + service_time
    waiting_time += service_time

sorted_jobs, waiting_times, total_time
