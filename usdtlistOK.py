import requests # type: ignore
import common_functions
domin_list = []
domin_list =  common_functions.readFile('domin')
print(len(domin_list))
token_list = []
token_list = common_functions.readFile('token')
if len(token_list) == 0:
    exit

for index in range(len(domin_list)):
    headers = {
    "Token":token_list[index],
    "lang": "en-us",
    }
    data = {
         "type": "usdt",
    } 
    print(data)
    try:
        response = requests.post(domin_list[index]+"/api/money/myusdt", data=data,headers=headers)  
        if response.status_code == 200:
            print(domin_list[index]+"===🍏");
            print(response);
            json = response.json()
            print(json['code'])
            try:
                print(json['data'])
            except Exception as e:
                print(e)
        else:
            print(domin_list[index]+"===🍎");   
               
    except Exception as e:
        print(f"第{index}个")
        print(domin_list[index]+"====🍎")
        print(str(phone_list[index])+"====🍎")
        print(e)


