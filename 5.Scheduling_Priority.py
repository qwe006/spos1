

totalprocess = int(input("Enter the number of processes: "))  
proc = []


for i in range(totalprocess):
    l = [0, 0, 0, 0]  
    proc.append(l)


def get_wt_time(wt):
    service = [0] * totalprocess  
    service[0] = proc[0][0]  
    wt[0] = 0 

    for i in range(1, totalprocess):
        
        service[i] = service[i - 1] + proc[i - 1][1]
        
        wt[i] = service[i] - proc[i][0]

        
        if wt[i] < 0:
            wt[i] = 0


def get_tat_time(tat, wt):
    for i in range(totalprocess):
        tat[i] = proc[i][1] + wt[i]  


def findgc():
    wt = [0] * totalprocess  
    tat = [0] * totalprocess  
    wavg = 0  
    tavg = 0  

    
    get_wt_time(wt)
    get_tat_time(tat, wt)

    stime = [0] * totalprocess  
    ctime = [0] * totalprocess  
    stime[0] = proc[0][0]  
    ctime[0] = stime[0] + proc[0][1]  

    
    for i in range(1, totalprocess):
        stime[i] = max(proc[i][0], ctime[i - 1])  
        ctime[i] = stime[i] + proc[i][1]  

    
    print("Process\tArrival\tPriority\tBurst\tStart\tComplete\tTurnaround\tWaiting")
    for i in range(totalprocess):
        wavg += wt[i]
        tavg += tat[i]
        print(f"P{proc[i][3]}\t{proc[i][0]}\t{proc[i][2]}\t\t{proc[i][1]}\t{stime[i]}\t{ctime[i]}\t\t{tat[i]}\t\t{wt[i]}")

    
    print(f"\nAverage Waiting Time: {wavg / totalprocess:.2f}")
    print(f"Average Turnaround Time: {tavg / totalprocess:.2f}")


if __name__ == "__main__":
    
    for i in range(totalprocess):
        arrivaltime = int(input(f"Enter arrival time for process {i + 1}: "))
        bursttime = int(input(f"Enter burst time for process {i + 1}: "))
        priority = int(input(f"Enter priority for process {i + 1} (lower number means higher priority): "))

        
        proc[i][0] = arrivaltime  # Arrival Time
        proc[i][1] = bursttime    # Burst Time
        proc[i][2] = priority     # Priority
        proc[i][3] = i + 1        # Process Number

    proc.sort(key=lambda x: (x[0], x[2]))

    # Calling function to generate Gantt chart and find scheduling details
    findgc()

#ouput
Enter the number of processes: 3
Enter arrival time for process 1: 0
Enter burst time for process 1: 5
Enter priority for process 1 (lower number means higher priority): 2
Enter arrival time for process 2: 1
Enter burst time for process 2: 3
Enter priority for process 2 (lower number means higher priority): 1
Enter arrival time for process 3: 2
Enter burst time for process 3: 8
Enter priority for process 3 (lower number means higher priority): 3
Process Arrival Priority        Burst   Start   Complete        Turnaround      Waiting
P1      0       2               5       0       5               5               0
P2      1       1               3       5       8               7               4
P3      2       3               8       8       16              14              6

Average Waiting Time: 3.33
Average Turnaround Time: 8.67