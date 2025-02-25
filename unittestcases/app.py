import requests
create_url = "https://reqres.in/api/users"
def add(x,y):
    try:
        return x+y
    except Exception as err:
        return None

def call_api_create(req_body):
    import pdb;pdb.set_trace()
    return requests.post(create_url, json=req_body)

class Customer:
    def __init__(self, id, name):
        self.id = id
        self.name=name
    def create_customer(self):
        req_body = {
            "name": "morpheus",
            "job": "leader"
        }
        resp = call_api_create(req_body)
        print("REQUEST PROCESSED..")
        resp_data = resp.json()
        if resp_data.get("status_code")==200:
            return "created"

    def update_customer(self):
        return "updated"

    def delete_customer(self):
        return "deleted"

