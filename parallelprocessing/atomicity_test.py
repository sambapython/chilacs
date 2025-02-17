from faker import Faker 
import time
import random
import threading
lock = threadin.Lock()
def write_data(data):
    f=open("data_thr.txt","a")
    with lock:
        for row in data:
            f.write(row)
            time.sleep(0.1)
            f.flush()
        f.close()

fak = Faker()
data = []
print("preparing data")
for i in range(10000):
    data.append(f"{i},{fak.name()},{random.randint(12345,678910)}\n")
print("preparing data completed")
offset=0
limit=5000
while True:
    part_data = data[offset:limit]#
    if not part_data:
        break
    thr = threading.Thread(target=write_data, args=(part_data,))
    thr.start()
    #write_data(part_data)
    offset = limit 
    limit = offset+limit
    time.sleep(2)

