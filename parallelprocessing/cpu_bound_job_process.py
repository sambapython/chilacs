import multiprocessing
import threading
import time
import os
def find_average():
    print("function executing:", os.getpid(), threading.current_thread().name)
    print(sum(list(range(20000000)))/20000000)



if __name__ == "__main__":
    print("program started:", os.getpid(), threading.current_thread().name)
    t1 = time.time()
    ps = []
    for i in range(4):
        thr = multiprocessing.Process(target=find_average, name="thread%s"%i)
        thr.start()
        ps.append(thr)
    t2=time.time()
    while ps:
        for p in ps:
            if not p.is_alive():
                ps.remove(p)
    
    print("TIME TAKEN:", t2-t1)
    print("program ending:",os.getpid(), threading.current_thread().name)
