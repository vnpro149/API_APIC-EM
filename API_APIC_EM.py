import requests
import json

def get_ticket():
    url="http://10.215.26.60/api/v1/ticket" # api get ticket
    header={
        "content-type":"application/json"
    }
    body=json.dumps({
        "username":"admin",
        "password":"vnpro@123"
    })
    response= requests.post(url=url,headers=header,data=body,verify=False)
    data=response.json()
    #print(data)
    ticket=data["response"]["serviceTicket"]
    print(ticket)
    return ticket

def get_list_device():
    url="http://10.215.26.60/api/v1/network-device" #api get list device
    header={
        "x-auth-token":get_ticket()
    }
    response= requests.get(url=url,headers=header,verify=False)
    data=response.json()
    print(data)
#get_ticket()
get_list_device()