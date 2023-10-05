import multiprocessing
import time
import random
from datetime import datetime

# Function to be executed by each process
def print_time_and_exit():
    sleep_time = random.randint(1, 5)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Process {multiprocessing.current_process().name} is sleeping for {sleep_time} seconds and started at {current_time}.")
    time.sleep(sleep_time)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Process {multiprocessing.current_process().name} woke up at {current_time} and is exiting.")

if __name__ == "__main__":
    # Create three separate processes
    processes = []

    for i in range(3):
        process = multiprocessing.Process(target=print_time_and_exit)
        processes.append(process)
        process.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()

    print("All processes have completed.")
