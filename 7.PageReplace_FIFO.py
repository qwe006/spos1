def fifo_page_replacement():
    
    noofpages = int(input("Enter the number of pages you want to enter: "))
    pages = list(map(int, input("Enter the pages (space-separated): ").split()))

    
    capacity = int(input("Enter the capacity of frame: "))
    frame = [-1] * capacity
    table = [[-1] * capacity for _ in range(noofpages)]
    
    hit = 0
    fault = 0
    index = 0

    print("\n----------------------------------------------------------------------")
   
    for i in range(noofpages):
        search = -1
        
        for j in range(capacity):
            if frame[j] == pages[i]:
                search = j
                hit += 1
                print(" H ", end="")
                break

        
        if search == -1:
            frame[index] = pages[i] 
            fault += 1
            print(" F ", end="")
            index += 1
            if index == capacity:
                index = 0  

        
        for j in range(capacity):
            table[i][j] = frame[j]

    print("\n----------------------------------------------------------------------")

    
    for i in range(capacity):
        for j in range(noofpages):
            if table[j][i] == -1:
                print("  - ", end="")
            else:
                print(f"{table[j][i]:3d}", end=" ")
        print()

    print("----------------------------------------------------------------------")

    
    fault_ratio = (fault / noofpages) * 100
    hit_ratio = (hit / noofpages) * 100
    print(f"Page Fault: {fault}\nPage Hit: {hit}")
    print(f"Hit Ratio: {hit_ratio:.2f}% \nFault Ratio: {fault_ratio:.2f}%")

# Run the function
fifo_page_replacement()


#output
# Enter the number of pages you want to enter: 20
# Enter the pages (space-separated): 1 2 3 4 2 1 5 6 2 1 2 3 7 6 3 2 1 3 3 6
# Enter the capacity of frame: 3

# ----------------------------------------------------------------------------------------------------------
#    F    F     F     F    H     F     F     F    F    F     H     F     F    F     H     F    F    F     H    F
# ----------------------------------------------------------------------------------------------------------
#    1     1     1     4     4     4     4     6     6     6     6     3     3     3     3     2     2     2     2     6
#    -      2     2     2     2     1     1     1     2     2     2     2     7     7     7     7     1     1     1     1
#    -     -      3     3     3     3     5     5     5     1     1     1     1     6     6     6     6     3     3     3
# ----------------------------------------------------------------------------------------------------------
# Page Fault: 16
# Page Hit: 4
# Hit Ratio: 20.00%
# Fault Ratio: 80.00%