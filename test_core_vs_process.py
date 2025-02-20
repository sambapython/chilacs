import time
import multiprocessing
def fun():
    time.sleep(10)
    print("done")

if __name__ == "__main__":
    ps = []
    for i in range(150):
        p=multiprocessing.Process(target=fun)
        ps.append(p)
        p.start()
        print(len(ps))
        time.sleep(0.01)
