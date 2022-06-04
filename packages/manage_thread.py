import threading
import math

def create_thread(thread_list, max_thread, target, args):
    args = list(args)
    work_per_thread =  math.floor(len(args) / max_thread)
    
    for n in range(0, max_thread):
        start = 0 if n == 0 else n * work_per_thread
        stop = (n + 1) * work_per_thread if n != max_thread - 1  else len(args)
        th = threading.Thread(target=target, args=(start, stop, args) , name=f'[Thread {n}]')
        thread_list.append(th)

def run(thread_list):
    for th in thread_list:
        th.start()

def end(thread_list, msg):
    for th in thread_list:
        th.join()
    print(msg)