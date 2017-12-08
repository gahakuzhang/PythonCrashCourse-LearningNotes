# 10.1 read from a file 从文件中读取数据
# 10.1.1 read an entire file 读取整个文件
with open('pi_digits.txt') as file_object:
    contents=file_object.read()
    print(contents)
# 关键字with让Python负责在合适的时候关闭文件
# open('file_name')打开文件
# 方法read()读取文件内容，作为字符串存在变量中，末尾有一个空字符串
# 使用rstrip()删除字符串末尾的空白
with open('pi_digits.txt') as file_object:
    contents=file_object.read()
    print(contents.rstrip())