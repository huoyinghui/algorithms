from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import os
import threading

def task():
    #task cpu
    # print('Executing our task on Process: {}'.format(os.getpid()))
    print('Executing our  task on Process: {} {}'.format(os.getpid(), threading.get_ident()))

def task_io():
    print('Executing our io task on Process: {} {}'.format(os.getpid(), threading.get_ident()))
    result = 0
    i = 0
    for i in range(10):
        result = result + i
    import time
    time.sleep(1)
    print("I: {}".format(result))
    print("Task Executed {}".format(threading.current_thread()))



def main():
    # executor = ProcessPoolExecutor(max_workers=2)
    # task1 = executor.submit(task)
    # task2 = executor.submit(task)
    # with ProcessPoolExecutor(max_workers=2) as executor:
    #     task1 = executor.submit(task)
    #     task2 = executor.submit(task)
    with ThreadPoolExecutor(max_workers=3) as executor:
        task1 = executor.submit(task_io)
        task2 = executor.submit(task_io)
    pass

if __name__ == '__main__':
    main()

# (math3) ➜  demo git: (hyh) ✗ time python demo_async.py
# Executing our io task on Process: 1897 123145402126336
# Executing our io task on Process: 1897 123145407381504
# I: 45
# I: 45
# Task Executed < Thread(ThreadPoolExecutor-0_0, started daemon 123145402126336) >
# Task Executed < Thread(ThreadPoolExecutor-0_1, started daemon 123145407381504) >
# python demo_async.py  0.07s user 0.02s system 7 % cpu 1.095 total
    
