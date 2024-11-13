# Practical 4

import threading
import time
import random

# Dining Philosophers Problem
def dining_philosophers():
    class Philosopher(threading.Thread):
        def __init__(self, index, left_fork, right_fork, iterations):
            threading.Thread.__init__(self)
            self.index = index
            self.left_fork = left_fork
            self.right_fork = right_fork
            self.iterations = iterations

        def run(self):
            for _ in range(self.iterations):
                print(f"Philosopher {self.index} is thinking.")
                time.sleep(random.random())
                print(f"Philosopher {self.index} is hungry.")
                self.eat()

        def eat(self):
            with self.left_fork:
                with self.right_fork:
                    print(f"Philosopher {self.index} is eating.")
                    time.sleep(random.random())
                    print(f"Philosopher {self.index} finished eating.")

    forks = [threading.Lock() for _ in range(5)]
    iterations = int(input("Enter number of iterations for each philosopher: "))
    philosophers = [Philosopher(i, forks[i % 5], forks[(i + 1) % 5], iterations) for i in range(5)]

    for p in philosophers:
        p.start()

    for p in philosophers:
        p.join()



# Main Function with Menu (Switch Case)
def main():
    print("2. Dining Philosophers Problem")
    print("\nRunning Dining Philosophers Problem...")
    dining_philosophers()
   

if __name__ == "__main__":
    main()




# Running Dining Philosophers Problem...
# Enter number of iterations for each philosopher: 5
# Philosopher 0 is thinking.
# Philosopher 1 is thinking.
# Philosopher 2 is thinking.
# Philosopher 3 is thinking.
# Philosopher 4 is thinking.
# Philosopher 4 is hungry.
# Philosopher 4 is eating.
# Philosopher 4 finished eating.
# Philosopher 4 is thinking.
# Philosopher 0 is hungry.
# Philosopher 0 is eating.
# Philosopher 4 is hungry.
# Philosopher 3 is hungry.
# Philosopher 2 is hungry.
# Philosopher 0 finished eating.
# Philosopher 0 is thinking.
# Philosopher 4 is eating.
# Philosopher 0 is hungry.
# Philosopher 1 is hungry.
# Philosopher 4 finished eating.
# Philosopher 4 is thinking.
# Philosopher 3 is eating.
# Philosopher 3 finished eating.
# Philosopher 3 is thinking.
# Philosopher 2 is eating.
# Philosopher 3 is hungry.
# Philosopher 4 is hungry.
# Philosopher 2 finished eating.
# Philosopher 2 is thinking.
# Philosopher 1 is eating.
# Philosopher 1 finished eating.
# Philosopher 1 is thinking.
# Philosopher 0 is eating.
# Philosopher 2 is hungry.
# Philosopher 0 finished eating.
# Philosopher 0 is thinking.
# Philosopher 4 is eating.
# Philosopher 1 is hungry.
# Philosopher 4 finished eating.
# Philosopher 4 is thinking.
# Philosopher 3 is eating.
# Philosopher 0 is hungry.
# Philosopher 4 is hungry.
# Philosopher 3 finished eating.
# Philosopher 3 is thinking.
# Philosopher 2 is eating.
# Philosopher 3 is hungry.
# Philosopher 2 finished eating.
# Philosopher 2 is thinking.
# Philosopher 1 is eating.
# Philosopher 1 finished eating.
# Philosopher 1 is thinking.
# Philosopher 0 is eating.
# Philosopher 2 is hungry.
# Philosopher 1 is hungry.
# Philosopher 0 finished eating.
# Philosopher 0 is thinking.
# Philosopher 4 is eating.
# Philosopher 4 finished eating.
# Philosopher 4 is thinking.
# Philosopher 3 is eating.
# Philosopher 0 is hungry.
# Philosopher 4 is hungry.
# Philosopher 3 finished eating.
# Philosopher 3 is thinking.
# Philosopher 2 is eating.
# Philosopher 3 is hungry.
# Philosopher 2 finished eating.
# Philosopher 2 is thinking.
# Philosopher 1 is eating.
# Philosopher 1 finished eating.
# Philosopher 1 is thinking.
# Philosopher 0 is eating.
# Philosopher 1 is hungry.
# Philosopher 2 is hungry.
# Philosopher 0 finished eating.
# Philosopher 0 is thinking.
# Philosopher 4 is eating.
# Philosopher 0 is hungry.
# Philosopher 4 finished eating.
# Philosopher 3 is eating.
# Philosopher 3 finished eating.
# Philosopher 3 is thinking.
# Philosopher 2 is eating.
# Philosopher 2 finished eating.
# Philosopher 2 is thinking.
# Philosopher 1 is eating.
# Philosopher 2 is hungry.
# Philosopher 3 is hungry.
# Philosopher 3 is eating.
# Philosopher 3 finished eating.
# Philosopher 1 finished eating.
# Philosopher 1 is thinking.
# Philosopher 2 is eating.
# Philosopher 0 is eating.
# Philosopher 0 finished eating.
# Philosopher 2 finished eating.
# Philosopher 1 is hungry.
# Philosopher 1 is eating.
# Philosopher 1 finished eating.

