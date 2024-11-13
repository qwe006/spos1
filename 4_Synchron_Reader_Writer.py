# Practical 4

import threading
import time
import random

# Readers-Writers Problem
def readers_writers():
    mutex = threading.Lock()
    write_block = threading.Lock()
    readers_count = 0
    read_operations = int(input("Enter number of read operations: "))
    write_operations = int(input("Enter number of write operations: "))

    def reader():
        nonlocal readers_count
        for _ in range(read_operations):
            mutex.acquire()
            readers_count += 1
            if readers_count == 1:
                write_block.acquire()
            mutex.release()

            print(f"Reader {threading.current_thread().name} is reading.")
            time.sleep(1)
            print(f"Reader {threading.current_thread().name} finished reading.")

            mutex.acquire()
            readers_count -= 1
            if readers_count == 0:
                write_block.release()
            mutex.release()

            time.sleep(1)

    def writer():
        for _ in range(write_operations):
            print(f"Writer {threading.current_thread().name} is waiting to write.")
            write_block.acquire()

            print(f"Writer {threading.current_thread().name} is writing.")
            time.sleep(2)
            print(f"Writer {threading.current_thread().name} finished writing.")

            write_block.release()
            time.sleep(1)

    for i in range(3):
        threading.Thread(target=reader, name=f'Reader-{i+1}').start()

    for i in range(2):
        threading.Thread(target=writer, name=f'Writer-{i+1}').start()

# Main Function with Menu (Switch Case)
def main():
    while True:

        print("3. Readers-Writers Problem")
     
        print("\nRunning Readers-Writers Problem...")
        readers_writers()
       
if __name__ == "__main__":
    main()




# Running Readers-Writers Problem...
# Enter number of read operations: 5
# Enter number of write operations: 3
# Reader Reader-1 is reading.
# Reader Reader-2 is reading.
# Reader Reader-3 is reading.
# Writer Writer-1 is waiting to write.
# Writer Writer-2 is waiting to write.

# --- Synchronization Problems Menu ---
# 1. Producer-Consumer Problem
# 2. Dining Philosophers Problem
# 3. Readers-Writers Problem
# 4. Exit
# Choose a problem to run (1-4): Reader Reader-2 finished reading.
# Reader Reader-1 finished reading.
# Reader Reader-3 finished reading.
# Writer Writer-1 is writing.
# Writer Writer-1 finished writing.
# Writer Writer-2 is writing.
# Writer Writer-1 is waiting to write.
# Writer Writer-2 finished writing.
# Reader Reader-1 is reading.
# Reader Reader-3 is reading.
# Reader Reader-2 is reading.
# Writer Writer-2 is waiting to write.
# Reader Reader-1 finished reading.
# Reader Reader-3 finished reading.
# Reader Reader-2 finished reading.
# Writer Writer-1 is writing.
# Writer Writer-1 finished writing.
# Writer Writer-2 is writing.
# Writer Writer-1 is waiting to write.
# Writer Writer-2 finished writing.
# Reader Reader-1 is reading.
# Reader Reader-3 is reading.
# Reader Reader-2 is reading.
# Writer Writer-2 is waiting to write.
# Reader Reader-1 finished reading.
# Reader Reader-3 finished reading.
# Reader Reader-2 finished reading.
# Writer Writer-1 is writing.
# Writer Writer-1 finished writing.
# Writer Writer-2 is writing.
# Writer Writer-2 finished writing.
# Reader Reader-2 is reading.
# Reader Reader-1 is reading.
# Reader Reader-3 is reading.
# Reader Reader-2 finished reading.
# Reader Reader-1 finished reading.
# Reader Reader-3 finished reading.
# Reader Reader-2 is reading.
# Reader Reader-1 is reading.
# Reader Reader-3 is reading.
# Reader Reader-2 finished reading.
# Reader Reader-1 finished reading.
# Reader Reader-3 finished reading.

#  -->