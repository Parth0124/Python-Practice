### two reasons: 1. I/O ops waiting time is more 2. Multiple actions concurrently

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number:{i}")

def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(f"letter: {letter}")

t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letter) ### created two threads for 2 different functions.

t=time.time()
t1.start()
t2.start()

t1.join()
t2.join()  ##join all the threads created.

finished_time=time.time()-t
print(finished_time)