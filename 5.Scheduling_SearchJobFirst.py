def sjf_preemptive_scheduling():
    processes = int(input("Enter the number of processes: "))

    arrival_times = [0] * processes
    burst_times = [0] * processes

    print("Enter the arrival times:")
    for i in range(processes):
        arrival_times[i] = int(input(f"Process {i + 1}: "))

    print("Enter the burst times:")
    for i in range(processes):
        burst_times[i] = int(input(f"Process {i + 1}: "))

    remaining_times = burst_times[:]
    completion_times = [0] * processes
    waiting_times = [0] * processes
    turnaround_times = [0] * processes

    time = 0
    completed = 0

    while completed < processes:
        min_remaining_time = float('inf')
        shortest_process = None

        # Find the process with the shortest remaining time
        for i in range(processes):
            if arrival_times[i] <= time and remaining_times[i] > 0:
                if remaining_times[i] < min_remaining_time:
                    min_remaining_time = remaining_times[i]
                    shortest_process = i

        # If no process is ready, move time forward
        if shortest_process is None:
            time += 1
            continue

        # Execute the selected process for 1 unit of time
        remaining_times[shortest_process] -= 1

        # If the process finishes, calculate times
        if remaining_times[shortest_process] == 0:
            completed += 1
            completion_times[shortest_process] = time + 1
            waiting_times[shortest_process] = (completion_times[shortest_process] - 
                                               arrival_times[shortest_process] - 
                                               burst_times[shortest_process])
            turnaround_times[shortest_process] = (waiting_times[shortest_process] + 
                                                  burst_times[shortest_process])

        time += 1

    # Calculate total waiting and turnaround times
    total_wt = sum(waiting_times)
    total_tt = sum(turnaround_times)

    # Print the results in table format
    print("\nProcess\t\tArrival\t\tBurst\t\tCompletion\t\tWaiting\t\tTurnaround")
    for i in range(processes):
        print(f"P{i + 1}\t\t{arrival_times[i]}\t\t{burst_times[i]}\t\t{completion_times[i]}\t\t\t{waiting_times[i]}\t\t\t{turnaround_times[i]}")

    print(f"\nAverage Waiting Time: {total_wt / processes:.2f}")
    print(f"Average Turnaround Time: {total_tt / processes:.2f}")

sjf_preemptive_scheduling()

#output
Enter the number of processes: 4
Enter the arrival times:
Process 1: 1
Process 2: 2
Process 3: 1
Process 4: 4
Enter the burst times:
Process 1: 3
Process 2: 4
Process 3: 2
Process 4: 4

Process         Arrival         Burst           Completion              Waiting         Turnaround
P1              1               3               6                       2                       5
P2              2               4               10                      4                       8
P3              1               2               3                       0                       2
P4              4               4               14                      6                       10

Average Waiting Time: 3.00
Average Turnaround Time: 6.25