import threading
import time
import os
print(os.getpid(), threading.current_thread().name)
def find_average():
    print(os.getpid(), threading.current_thread().name)
    print(sum(list(range(20000000)))/20000000)
t1 = time.time()
for i in range(4):
    thr = threading.Thread(target=find_average, name="thread%s"%i)
    thr.start()
    thr.join()
    # find_average()
t2=time.time()
print("TIME TAKEN:", t2-t1)