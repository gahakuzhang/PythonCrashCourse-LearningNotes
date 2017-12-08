# 10.files and exceptions 文件和异常
# 10.1 read from a file 从文件中读取数据
# 10.1.1 read an entire file 读取整个文件
with open('pi_digits.txt') as file_object:
    contents=file_object.read()
    print(contents)
# 关键字with让Python负责在合适的时候关闭文件
# open('file_name')打开文件
# 方法read()读取文件内容，作为字符串存在变量中，末尾有一个空字符串filename='programming.txt'
with open(filename,'w') as file_object:
    file_object.write("I love programming!")
# 使用rstrip()删除字符串末尾的空白
with open('pi_digits.txt') as file_object:
    contents=file_object.read()
    print(contents.rstrip())

# 10.1.2 file paths 文件路径
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
# 原始字符串即不包括任何转义字符

# 10.1.3 read line by line 逐行读取
filename='pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
    print(line)
# 每行之间都会出现空白行，消除方法仍是使用rstrip()

# 10.1.4 make a list of lines from a file 创建一个包含文件各行内容的列表
filename='pi_digits.txt'
with open(filename) as file_object:
    lines=file_object.readlines()
for line in lines:
    print(line.rstrip())
# open()返回的文件对象只在with代码块内可用
# readlines()读取文件每一行，将其存储在一个列表中
# 在关键字with代码块之外，该列表仍然可用

# 10.1.5 work with a file's contents 使用文件内容
filename='pi_digits.txt'
with open(filename) as file_object:
    lines=file_object.readlines()
pi_string=''
for line in lines:
    pi_string+=line.rstrip()
print(pi_string)
print(len(pi_string))
# 注意输出结果没有空行，但有空格
# 删除空格用strip()
# txt会被默认看成是字符串，若要当成数值使用，需要使用int()或float()

# 10.1.6 large files: one million digits包含一百万位的大型文件
filename='pi_million_digits.txt'
with open(filename) as file_object:
    lines=file_object.readlines()
pi_string=''
for line in lines:
    pi_string+=line.strip()
print(pi_string)
print(len(pi_string))

# 10.1.7 is your birthday contained in Pi 圆周率中包含你的生日吗
filename='pi_million_digits.txt'
with open(filename) as file_object:
    lines=file_object.readlines()
pi_string=''
for line in lines:
    pi_string+=line.strip()
birthday=input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi!")


# 10.2 write to a file 写入文件
# 10.2.1 write to an empty file 写入空文件
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming!")
# 调用open()时提供了2个实参，第一个实参是要打开的文件名，第二个实参'w'代表写入模式
# 模式实参：'r'读取模式 'w'写入模式 'a'附件模式 'r+'读取和写入模式；若省略，默认只读模式
# 如果文件不存在，open()将自动创建
# 'w'将在返回文件对象前清空该文件

# 10.2.2 write multiple lines 写入多行
# write()不会主动添加换行符。要利用换行 空格 制表符
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming!\n")
    file.object.write("I love creating new games.\n")

# 10.2.3 append to a file 附加到文件
# 添加而不是覆盖原有内容，使用附加模式
filename = 'programming.txt'
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a brower.\n")


# 10.3 exceptions 异常
# 10.3.1 handle the ZeroDivisionError exception 处理ZeroDivisionError异常
print(5/0)
# ZeroDivisionError是一个异常对象

# 10.3.2 use try-except blocks 使用try-except代码块
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by 0!")

# 10.3.3 use exceptions to prevent crashes 使用异常避免崩溃
# 10.3.4 the else block else代码块
# try-except-else代码原理：可能引发异常的代码放在try语句中
# 仅在try语句成功执行时才需要运行的代码放在else代码块中
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number=input("\nFirst number: ")
    if first_number=='q':
        break
    second_number=input("\nSecond number: ")
    try:
        answer=int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("you can't divide 0!")
    else:
        print(answer)

# 10.3.5 handle the FileNotFoundError Exception 处理FileNotFoundError异常
filename='alice.txt'
try:
    with open(filename) as f_obj:
        contents=f_obj.read()
except FileNotFoundError:
    msg="Sorry, the file "+filename+" does not exist."
    print(msg)

# 10.3.6 analyze text 分析文本
# split()以空格为分隔符拆分字符串，并存储在一个列表中。
filename='alice.txt'
try:
    with open(filename) as f_obj:
        contents=f_obj.read()
except FileNotFoundError:
    msg="Sorry, the file "+filename+" does not exist."
    print(msg)
else:
    # 计算文件中包含多少个单词HB
    words=contents.split()
    num_words=len(words)
    print("The file "+filename+" has about "+str(num_words)+" words.")

# 10.3.7 work with multiple files 使用多个文件
def count_words(filename):
    # 计算文件中包含多少个单词
    try:
        with open(filename) as f_obj:
            contents=f_obj.read()
    except FileNotFoundError:
        msg="Sorry, the file "+filename+" does not exist."
        print(msg)
    else:
        words=contents.split()
        num_words=len(words)
        print("The file "+filename+" has about "+str(num_words)+" words.")

filenames = ['alice.txt','siddhartha.txt','moby_dick.txt','little_women.txt']
for filename in filenames:
    count_words(filename)

# 10.3.8 fail silently 失败时一声不吭
# pass语句
def count_words(filename):
    # 计算文件中包含多少个单词
    try:
        with open(filename) as f_obj:
            contents=f_obj.read()
    except FileNotFoundError:
        pass
    else:
        words=contents.split()
        num_words=len(words)
        print("The file "+filename+" has about "+str(num_words)+" words.")

filenames = ['alice.txt','siddhartha.txt','moby_dick.txt','little_women.txt']
for filename in filenames:
    count_words(filename)

# 10.3.9 decide which errors to report 决定报告哪些错误


# 10.4 store data 存储数据
# json模块将Python数据结构存储在文件中并在程序再次运行时加载改文件中的数据

# 10.4.1 use json.dump() and json.load()
import json
numbers=[2,3,5,7,11,13]
filename='numbers.json'
with open(filename,'w') as f_obj:
    json.dump(numbers,f_obj)
# 先导入模块json
# json.dump()接受两个实参：要存储的数据和用于存储的文件对象
# with open(filename,'w') as f_obj 以写入模式打开文件，让json能够将数据写入其中

# 使用json.load()将该列表读取到内存中
import json
filename='numbers.json'
with open(filename) as f_obj:
    numbers=json.load(f_obj)
print(numbers)
# with open(filename) as f_obj:使用的是读取模式

# 10.4.2 save and read user-generated data 保存和读取用户生成的数据
# 写这段代码时出了很多错误
import json
filename='username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username=input("What is your name? ")
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
        print("We'll remember you when you come back, "+username+"!")
else:
    print("Welcome back, "+username+"!")

# 10.4.3 refactor 重构
# 重构：将代码划分成一系列函数
import json
def get_stored_username():
    """如果存储了用户名则获取它"""
    filename='username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """提示用户输入用户名"""
    username=input("What is your name? ")
    filename='username.json'
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
    return username

def greet_user():
    """问候用户，指出名字"""
    username=get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username=get_new_username()
        print("We'll remember you when you come back, "+username+"!")

greet_user()