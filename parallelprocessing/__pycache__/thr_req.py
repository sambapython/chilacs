import pdb;pdb.set_trace()
import requests
import time
import threading
print("requesting for user creation")
create_url = "https://reqres.in/api/users"

def update(user_data):
    single_user_url = create_url+"/"+str(user_data["id"])
    data = {"name": user_data["first_name"].upper()}
    resp = requests.put(single_user_url, json=data)
    print(resp.json())

users_data = []
for page in range(1,3):
    list_user_url = create_url+"/?page=%s"%page
    resp = requests.get(list_user_url)
    users_data.extend(resp.json()["data"])
t1=time.time()
for user_data in users_data:
    update(user_data)
t2=time.time()
print(t2-t1)

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