import threading
from collections import deque
import time
d=deque()
#d=[]
def trigger_producer():
    c=0
    print("PRODUCER STARTED")
    while True:
        threading.Thread(target=producer, args=(c,)).start()
        c=c+1
        time.sleep(0.5)

def trigger_consumer():
    print("CONSUMER STARTED")
    while True:
        threading.Thread(target=consumer).start()
        time.sleep(0.5)
def producer(x):
    print(f"Adding {x} to the queue")
    d.append(x)

def consumer():
    element = d.pop()
    print(f"Consumer got an element: {element}")

thr = threading.Thread(target=trigger_producer).start()
thr = threading.Thread(target=trigger_consumer).start()

