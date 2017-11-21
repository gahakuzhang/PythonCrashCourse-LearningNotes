#4.5.3 writing over a tuple 修改元组变量
dimensions=(200,50)
print('original dimensions:')
for dimension in dimensions:
    print(dimension)
dimensions=(400,100)
print('\nModified dimensions:')
for dimension in dimensions:
    print(dimension)
#不能修改元组的元素，但是可以给元组变量赋新值