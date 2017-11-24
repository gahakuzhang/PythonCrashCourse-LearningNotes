#7.2.3 using a flag 标志
# 注意True和False首字母要大写
prompt="\nTell me something, and I will repeat it back to u: "
prompt+="\nEnter 'quit' to end of this program. "
active=True
while active:
    message = input(prompt)
    if message=='quit':
        active=False
    else:
        print(message)

