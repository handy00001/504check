import requests  # type: ignore
import common_functions

domin_list = []
domin_list = common_functions.readFile('domin')

phone_list = []
phone_list = common_functions.readFile('phone')

print(len(domin_list))
print(len(phone_list))

token_list = []
for index in range(len(domin_list)):
    data = {
        "username": "91" + str(phone_list[index]),
        "type": 8,
        "password": "e10adc3949ba59abbe56e057f20f883e",
        "county": "91",
    }

    try:
        response = requests.post(domin_list[index] + "/api/login/in", data=data)
        if response.status_code == 200:
            print("第" + str(index) + "个")
            print(domin_list[index] + "===🍏")
            json = response.json()
            print(json["code"])
            try:
                print(json["data"]["token"])
                token_list.append(json["data"]["token"])
            except Exception as e:
                print(e)
        else:
            print(domin_list[index] + "===🍎")
    except Exception as e:
            print(e)


print(token_list)


try:
    with open("token.txt", "w") as file:
    # 遍历数组中的元素，并将其逐行写入文件
      for item in token_list:
          file.write(str(item) + "\n")

          
except Exception as e:
    print