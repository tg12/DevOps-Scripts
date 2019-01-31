import threading
import random

def worker(thread_no, rand_int):
    print ('I am thread: ' + str(thread_no) + '\n')
    print ("My random number is ..." + str(rand_int))

thread_list = []
for thread_no in range(7000):
    rand_int = random.randint(1,9999)
    thread = threading.Thread(target=worker, args=(thread_no,rand_int))
    thread_list.append(thread)
    thread.start()