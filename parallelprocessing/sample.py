import threading
import time
from collections import queue

print("program started")
count=0
max_thread_count=10
thrs = []
def wait():
    current_thread = threading.current_thread().name
    f=open(f"data\data_{current_thread}.txt","a")
    for i in range(4):
        f.write(str(i))
        f.write("\n")
        time.sleep(1)
    f.close()
for i in range(5):
    thr = threading.Thread(target=wait, name="thread%s"%count)
    print(thr.name, "created")
    thr.start()
    count = count+1



    """
    if len(thrs)==max_thread_count:
        for thr in thrs:
            thr.join()#1-2-3-4-5-6-7-8-9-10
            print("ACTIVE THREADS:", threading.active_count())
        thrs=[]
        print("DONE WITH ALL 10 threads")
    while len(thrs)>=max_thread_count:
        print("ACTIVE THREADS:", threading.active_count())
        for thr in thrs:
            if not thr.is_alive():
                thrs.remove(thr)
        time.sleep(0.1)
    """

        


