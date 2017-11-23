#6.3.4 遍历所有value
#使用values()
favorite_idols={
    'ghk':'nachan',
    'yc':'kazumin',
    'a':'maiyan',
    'b':'erika',
    }
print('The idols have been mentioned: ')
for idol in favorite_idols.values():
    print(idol.title())
#另一种写法
#for name in favorite_idols:
    #print(favorite_idols[name].title())

#使用set剔除重复项，提取字典中独一无二的元素
favorite_idols={
    'ghk':'nachan',
    'yc':'kazumin',
    'a':'nachan',
    'b':'nachan',
    }
print('The idols have been mentioned: ')
for idol in set(favorite_idols.values()):
    print(idol.title())