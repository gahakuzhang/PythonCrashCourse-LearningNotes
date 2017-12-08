# 10.4.1 use json.dump() and json.load()
import json
numbers=[2,3,5,7,11,13]
filename='numbers.json'
with open(filename,'w') as f_obj:
    json.dump(numbers,f_obj)
# 先导入模块json
# json.dump()接受两个实参：要存储的数据和用于存储的文件对象
# with open(filename,'w') as f_obj 以写入模式打开文件，让json能够将数据写入其中