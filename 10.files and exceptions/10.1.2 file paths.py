# 10.2 file paths 文件路径
# 相对文件路径：当前执行的文件和text_files在一个文件夹
# Linux和OS X
with open('text_files/filename.txt') as file_object:
# Windows
with open(r'text_files\filename.txt') as file_object:

# 绝对文件路径
# Linux和OS X
file_path='/home/other_files/text_files/filename.txt'
with open(file_path) as file_object:
# Windows
file_path = r'C:\Users\other_files\text_files\filename.txt'
with open(file_path) as file_object:
# Windows应该用原始字符串的方式指定路径，即''前加上r