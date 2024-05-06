# common_functions.py

def readFile(name):
    """
    Greet a person by their name.
    """
    # print(f"Hello, {name}!")
    txt_name = name+".txt"
    # 打开文本文件以进行读取
    list = []
    with open(txt_name, "r") as file:
        # 读取文件中的每一行，并将其作为字符串存储在 lines 列表中
        domin_lines = file.readlines()
        # 遍历 lines 列表中的每一行
        for line in domin_lines:
        # 去除每行两端的空格和换行符，并将结果转换为对应的数据类型
            value = line.strip()
        # 将数据添加到数组中
            list.append(value)
            
    return list


def writeListDataToFile(list,name):
    """
    写文件 会覆盖之前的
    """
    txt_name = name+".txt"
    try:
        with open(txt_name, "w") as file:
        # 遍历数组中的元素，并将其逐行写入文件
            for item in list:
                file.write(str(item) + "\n")
        
        return "yes"
          
    except Exception as e:
        print(e)
        return "NO"




def writeListDataToFileW(list,name):
    """
    Add two numbers.
    """
    txt_name = name+".txt"
    try:
        with open(txt_name, "a") as file:
        # 遍历数组中的元素，并将其逐行写入文件
            for item in list:
                file.write(str(item) + "\n")
        
        return "yes"
          
    except Exception as e:
        print(e)
        return "NO"

