import threading
import time
data = list(range(2000))
res=[]
def add_list(l,x):
    time.sleep(0.1)
    l.append(x**2)

def add_list(l,x):
    time.sleep(0.1)
    l.append(x**2)

def add_file(x):
    time.sleep(0.1)
    f=open("data.txt","a")
    f.write(str(x**2)+",")
    f.close()

for i in data:
    # threading.Thread(target=add_list, args=(res, i)).start()
    threading.Thread(target=add_file, args=(i, )).start()
print(res)

