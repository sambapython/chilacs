import threading
import time

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
    thr = threading.Thread(target=wait, name="thread%s"%count, daemon=True)
    print(thr.name, "created")
    thr.start()
    count = count+1


        


