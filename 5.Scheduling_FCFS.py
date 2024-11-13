def fcfs_scheduling():
    processes = int(input("Enter the number of processes (up to 6): "))

    bt = [0] * processes  
    wt = [0] * processes  
    tt = [0] * processes  
    arrival_times = list(range(processes))  

    print("Enter burst times:")
    for i in range(processes):
        bt[i] = int(input(f"Process {i + 1}: "))

    
    exit_times = [0] * processes
    for i in range(processes):
        if i == 0:
            exit_times[i] = arrival_times[i] + bt[i]  
        else:
            exit_times[i] = max(arrival_times[i], exit_times[i - 1]) + bt[i]  

        tt[i] = exit_times[i] - arrival_times[i]  
        wt[i] = tt[i] - bt[i]  

    
    total_wt = sum(wt)
    total_tt = sum(tt)

    
    print("\nProcess\tBurst Time\tArrival Time\tWaiting Time\tTurnaround Time")
    for i in range(processes):
        print(f"{i + 1:<7}\t{bt[i]:<12}\t{arrival_times[i]:<14}\t{wt[i]:<14}\t{tt[i]:<15}")

    
    print("\nAverage waiting time and average turnaround time respectively:")
    print(f"Average Waiting Time: {total_wt / processes:.2f}")
    print(f"Average Turnaround Time: {total_tt / processes:.2f}")

# Call the function to execute
fcfs_scheduling()

#output
#Enter the number of processes (up to 6): 5
#Enter burst times:
#Process 1: 4
#Process 2: 3
#Process 3: 1
#Process 4: 2
#Process 5: 5

#Process Burst Time      Arrival Time    Waiting Time    Turnaround Time
#1       4               0               0               4
#2       3               1               3               6
#3       1               2               5               6
#4       2               3               5               7
#5       5               4               6               11

#Average waiting time and average turnaround time respectively:
#Average Waiting Time: 3.80
#Average Turnaround Time: 6.80
