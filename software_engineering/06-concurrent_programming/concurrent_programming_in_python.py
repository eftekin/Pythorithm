# Concurrent Programming in Python
import asyncio
import multiprocessing

# Section 2: The Threading Module
# The `threading` module is used to create and manage threads in Python.
import threading
import time

# Section 1: Introduction
# Concurrent programming is used to perform multiple tasks at the same time.
# This is achieved through threads, asynchronous programming, or multiple processes.


def print_numbers():
    for i in range(5):
        print(f"Number: {i}")
        time.sleep(1)  # Simulate a time-consuming task


# Creating a thread for running the `print_numbers` function
thread = threading.Thread(target=print_numbers)
thread.start()  # Starts the thread

# Section 3: Using Multiple Threads
# Multiple threads can be created to run separate tasks concurrently.


def print_letters():
    for letter in "abcde":
        print(f"Letter: {letter}")
        time.sleep(1)


# Creating another thread to run a different task
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

thread1.start()
thread2.start()

# Both tasks run concurrently

# Section 4: Joining a Thread
# The `join()` method is used to wait for a thread to complete before proceeding with the next steps in the program.
thread1.join()  # Wait for thread1 to finish
thread2.join()  # Wait for thread2 to finish

# Section 5: The Asyncio Module
# The `asyncio` module is used to write asynchronous programs in Python.
# It allows you to run tasks asynchronously using `async` and `await` keywords.


async def async_task():
    print("Starting async task...")
    await asyncio.sleep(2)  # Simulate an async task with a 2-second delay
    print("Async task complete.")


# Running the async task
async def main():
    await async_task()


# asyncio.run() is used to run the main function in an event loop.
asyncio.run(main())

# Section 6: Multiple Asynchronous Tasks
# You can run multiple asynchronous tasks concurrently using `asyncio.gather`.


async def async_task_1():
    print("Task 1 started")
    await asyncio.sleep(1)
    print("Task 1 complete")


async def async_task_2():
    print("Task 2 started")
    await asyncio.sleep(2)
    print("Task 2 complete")


async def run_multiple_tasks():
    await asyncio.gather(async_task_1(), async_task_2())


# Running multiple async tasks
asyncio.run(run_multiple_tasks())

# Section 7: The Multiprocessing Module
# The `multiprocessing` module allows you to run multiple processes instead of threads.
# This is useful for CPU-bound tasks where multiple processes can take advantage of multiple CPU cores.


def process_task():
    print("Starting process task...")
    time.sleep(2)
    print("Process task complete.")


if __name__ == "__main__":
    # Creating a process
    process = multiprocessing.Process(target=process_task)
    process.start()  # Start the process
    process.join()  # Wait for the process to complete

# Section 8: Using Multiple Processes
# Similar to threading, you can create multiple processes to run separate tasks concurrently.


def process_task_1():
    print("Process 1 task...")
    time.sleep(2)
    print("Process 1 complete.")


def process_task_2():
    print("Process 2 task...")
    time.sleep(1)
    print("Process 2 complete.")


if __name__ == "__main__":
    # Creating multiple processes
    process1 = multiprocessing.Process(target=process_task_1)
    process2 = multiprocessing.Process(target=process_task_2)

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("Both processes are done.")

# This demonstrates how multiprocessing can be used to parallelize tasks across multiple CPU cores.
