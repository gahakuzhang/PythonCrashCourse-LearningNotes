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
    # 计算文件中包含多少个单词
    words=contents.split()
    num_words=len(words)
    print("The file "+filename+" has about "+str(num_words)+" words.")