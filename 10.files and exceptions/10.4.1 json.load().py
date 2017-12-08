# 使用json.load()将该列表读取到内存中
import json
filename='numbers.json'
with open(filename) as f_obj:
    numbers=json.load(f_obj)
print(numbers)
# with open(filename) as f_obj:使用的是读取模式