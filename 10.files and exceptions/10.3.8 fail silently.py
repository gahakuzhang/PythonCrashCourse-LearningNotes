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