import requests
import json

url='http://10.215.26.60/api/v1'
account={
    'username':'admin',
    'password':'vnpro@123'
}
def get_ticket():
    urlticket=url+'/ticket'
    print(urlticket)
    header={
        'Content-type':'application/json'
    }
    response=requests.post(url=urlticket,headers=header,data=json.dumps(account),verify=False)
    print(response.json())
    ticket=response.json()['response']['serviceTicket']
    return ticket

def get_list_device():
    urlldevice=url+"/network-device"
    header={
        'X-Auth-Token': get_ticket()
    }
    response=requests.get(url=urlldevice,headers=header,verify=False)
    print(response.json())
    return response.json()


# get_list_device()
# get_ticket()
# demoticket=get_ticket()
# print(demoticket)

def get_id(ip):
    response=get_list_device()
    for i in response['response']:
        # print(i['managementIpAddress'])
        if i['managementIpAddress']==ip:
            return i['id']
    return None



def get_device(id):
    urlldevice=url+"/network-device/{}".format(id)
    header={
        'X-Auth-Token': get_ticket()
    }
    response=requests.get(url=urlldevice,headers=header,verify=False)
    print(response.json())
    return response.json()

def add_device(data):
    urladddevice=url+'/network-device'
    header={
        'X-Auth-Token': get_ticket(),
        'Content-type':'application/json'
    }
    resp=requests.post(url=urladddevice,headers=header,data=json.dumps(data),verify=False)

def del_device(ip):
    id=get_id(ip)
    urldel=url+'/network-device/{}'.format(id)
    header={
        'X-Auth-Token': get_ticket(),
        'Content-type':'application/json'
    }
    resp=requests.delete(url=urldel,headers=header,verify=False)

ticket=get_ticket() # Gọi đến hàm lấy ticket
print(ticket)
ldevice=get_list_device() #Gọi đến hàm lấy tất cả các thiết bị đang được quản lý trong APIC-EM
print(ldevice)
id=get_id("10.215.26.77") #Gọi đến hàm lấy id của thiết bị dựa vào địa chỉ ip của thiết bị đó
print(id)
infodevice=get_device(id=id) # Gọi đến hàm lấy thông tin thiết bị dựa vào số id
print(infodevice)
data={ # khai báo biến chứa thông tin cấu hình thiết bị
  "userName": "vnpro",
  "cliTransport": "ssh",
  "password": "vnpro@123",
  "snmpROCommunity": "public",
  "snmpRetry": 3,
  "snmpTimeout": 5,
  "snmpVersion": "v2",
  "snmpRWCommunity": "private",
  "ipAddress": [
    "10.215.27.137"
  ],
  "enablePassword": "vnpro@321"
}
# add_device(data=data)# Thêm thiết bị vào APIC-EM

# del_device("10.215.27.137") # Xóa thiết bị khỏi APIC-EM theo địa chỉ IP