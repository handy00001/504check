import requests # type: ignore
import common_functions

domin_list = []
domin_list = common_functions.readFile('domin')
print(len(domin_list))
token_list = []
token_list = common_functions.readFile('token')

print(len(domin_list))
if len(token_list) == 0 :
    exit

for index in range(len(domin_list)):
    headers = {
    "Token":token_list[index],
    "lang": "en-us",
    }
    data = {"page":1,"limit":20,"range":0}
    print(domin_list[index]+"/api/task/list")
    print(headers)
    try:       
        response = requests.post(domin_list[index]+"/api/task/list",data=data,headers=headers)  
        if response.status_code == 200:
            print("第 "+str(index)+" 个 == "+domin_list[index]+"===🍏");
            print(response);
            json = response.json()
            print(json['code'])
            print('info=='+json['info'])
            try:
              taskList =   json['data']["list"]
              print(taskList[0]["title"])
            except Exception as e:
                print(e)
        else:
            print(domin_list[index]+"===🍎");   
    
    except Exception as e:
            print(e)   


