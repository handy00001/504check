import requests # type: ignore
import common_functions

domin_list = []
domin_list =  common_functions.readFile('download')

for index in range(len(domin_list)):
    print('开始'+str(index))
    try:
      response = requests.get(domin_list[index])
      if response.status_code == 200:
            print("第"+str(index)+"个"+"🍏")
            print(response.headers)
      else:
            print("第"+str(index)+"个"+domin_list[index]+"===🍎")         
    except Exception as e:
       print("第"+str(index)+"个"+"💣")
       print(domin_list[index]+"===💣") 
       
    print('结束'+str(index))


