import requests
import time
import threading
print(threading.active_count(), "threads created")
print("program started")
create_url = "https://reqres.in/api/users"

def update(user_data):
    current_thread = threading.current_thread().name
    print(current_thread,"is executing the update function now")
    single_user_url = create_url+"/"+str(user_data["id"])
    data = {"name": user_data["first_name"].upper()}
    resp = requests.put(single_user_url, json=data)
    print(current_thread, resp.json())

users_data = []
for page in range(1,3):
    list_user_url = create_url+"/?page=%s"%page
    resp = requests.get(list_user_url)
    users_data.extend(resp.json()["data"])
t1=time.time()
count=1
thrs = []
for user_data in users_data:
    thr = threading.Thread(target=update, args=(user_data, ), name="thread%s"%count)# the update function called with the thread we created
    thr.start()
    thrs.append(thr)
    count = count+1
    #update(user_data) # called with main thread
for thr in thrs:
    print(thr.is_alive())
print(threading.active_count(), "threads are executing now")

t2=time.time()
print("time taken to complete the task:",t2-t1)



"""
#USER CREATION
req_body = {
    "name": "morpheus",
    "job": "leader"
}
resp = requests.post(create_url, json=req_body)
print("REQUEST PROCESSED..")
resp_data = resp.json()

#SINGLE USER GET CALL
user_id = resp_data["id"]
single_user_url = create_url+"/"+user_id
print(single_user_url)
resp = requests.get(single_user_url)
print(resp.json())
"""