import requests # type: ignore
import common_functions

domin_list = []
domin_list =  common_functions.readFile('domin')

for index in range(len(domin_list)):
    print('开始'+str(index))
    try:
      headers = {"lang": "en-us",}
      response = requests.post(domin_list[index]+"/api/login/index", data={},headers=headers)
      if response.status_code == 200:
            print("第"+str(index)+"个"+"🍏")
            print(domin_list[index])
            json = response.json()
            print(json)       
      else:
            print("第"+str(index)+"个"+domin_list[index]+"===🍎")         
    except Exception as e:
       print("第"+str(index)+"个"+"💣")
       print(domin_list[index]+"===💣") 
       
    print('结束'+str(index))


