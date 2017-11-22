#5.3.3 if-elif-else结构
#不简洁的版本
age=12
if age<4:
    print('Your admission cost is $0.')
elif age<18:
    print('Your admission cost is $5.')
else:
    print('Your admission cost is 10.')

#简洁的写法
age=20
if age<4:
    price=0
elif age<18:
    price=5
else:
    price=10
print('Your admission cost is $'+str(price)+'.')
