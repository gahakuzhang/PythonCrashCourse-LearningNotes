#7.2.2 letting the user choose when to quit
#充分理解程序运行的顺序
prompt="\nTell me something, and I will repeat it back to u: "
prompt+="\nEnter 'quit' to end of this program. "
message=""
while message!='quit':
    message=input(prompt)
    if message!='quit':
        print(message)
#首次执行while时，因为用户还没有输入，无法比较。因为先定义一个空字符串进行比较
#错误示例，以下程序会进入死循环
#同时input的位置也是错的，创建多行字符串的时候不应写入input()
#prompt=input("\nTell me something, and I will repeat it back to u: ")
#prompt+="\nEnter 'quit' to end of this program. "
#while prompt!='quit':
    #print(prompt)

