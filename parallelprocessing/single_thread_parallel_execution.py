import time
import asyncio
import threading
async def fun(x):
    print(f"function execution started by {x} {threading.current_thread().name}")
    await asyncio.sleep(5)
    return 10*x
async def main():
    print("program execution started")
    tasks = [fun(1), fun(2), fun(3), fun(4)]
    res = asyncio.gather(*tasks)
    for i in res:
        print(i)
    print("program execution ended")
t1 = time.time()
res = asyncio.run(main())
t2=time.time()
print(t2-t1)



