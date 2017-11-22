#4.4.3 copying a list 复制列表-不使用切片
my_idols=['nanamin','rentan','yuki']
#此路不通
yc_idols=my_idols
my_idols.append('miona')
yc_idols.append('kazumin')
print('My favorite members are:')
print(my_idols)
print('\nyc\'s favorite members are:')
print(yc_idols)
