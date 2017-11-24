#7.2.5 using continue in a loop
#满足if条件时continue忽略剩下的代码返回代码的开头
#不满足时继续执行余下的代码
#break不执行余下的代码并退出整个循环
current_number=0
while current_number<10:
    current_number+=1
    if current_number % 2==0:
        continue
    print(current_number)
