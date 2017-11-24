#7.2.4 using break to exit a loop
#while True开头的循环会的不断运行，直到遇到break
#break不执行余下的代码并退出整个循环
prompt="\nPlease enter the name of cities you have visited: "
prompt+="\n(Enter 'quit' when you are finished.) "
while True:
    city=input(prompt)
    if city=='quit':
        break
    else:
        print("I'd love to go to "+city.title()+"!")

