import multiprocessing
d={}
def add_element(x):
    print(f"add element: {x}")
    d.update({x:x**2})
    print("d in function:",d)
if __name__ == "__main__":
    process=[]
    for i in range(4):
        p = multiprocessing.Process(target=add_element, args=(i,))
        p.start()
        process.append(p)
    while process:
        for proc in process:
            if not proc.is_alive():
                process.remove(proc)
                break

    print(d)