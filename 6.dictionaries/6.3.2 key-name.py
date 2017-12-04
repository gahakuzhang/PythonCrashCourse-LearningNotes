#6.3.2 遍历所有键
#使用keys(),keys()可以省略
favorite_idols={
    'ghk':'nachan',
    'yc':'kazumin',
    'A':'maiyan',
    'B':'erika',
    }
for name in favorite_idols.keys():
    print(name.title())

#注意favorite_idols[name]的用法，不需要另外定义idol
favorite_idols={
    'ghk':'nachan',
    'yc':'kazumin',
    'A':'maiyan',
    'B':'erika',
    }
iihito=['ghk','yc']
for name in favorite_idols.keys():
    print(name)
    if name in iihito:
        print("Hi "+name.title()+
              " , thanks for supporting "+
              favorite_idols[name].title()+".")
