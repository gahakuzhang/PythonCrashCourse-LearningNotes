#5.3.6测试多个条件
requested_topping=['mushrooms','extra cheese']
if 'mushrooms' in requested_topping:
    print('Adding mushrooms.')
if 'pepperoni' in requested_topping:
    print('Adding pepperoni.')
if 'extra cheese' in requested_topping:
    print('Adding extra cheese.')
# 运行多个代码块时不能使用if-elif-else结构，因为if一旦通过将跳过if-elif-else结构余下的测试
# 运行多个代码块时需要使用一系列独立的if语句