import requests # type: ignore
import common_functions
domin_list = []
domin_list =  common_functions.readFile('domin')
phone_list = []
phone_list = common_functions.readFile('phone')
print(len(domin_list))
print(len(phone_list))

for index in range(len(domin_list)):
    dominnames = domin_list[index].split('//') 
    data = {"mobile":'91'+str(phone_list[index]),"scene":"register","county":"91"}
    print(data)
    try:
        response = requests.post(domin_list[index]+"/api/login/smsSend", data=data)  
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


