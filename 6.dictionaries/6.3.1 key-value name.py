#6.3.1 使用items.()
#遍历字典时，键值对的返回顺序和存储顺序不同(乱序)
idol_name1={
    'username':'73',
    'first_name':'nanami',
    'last_name':'hashimoto',
    }
for key,value in idol_name1.items():
    print('\nkey: '+key)
    print('value: '+value)

favorite_idols={
    'ghk':'nachan',
    'yc':'kazumin',
    'A':'maiyan',
    'B':'erika',
    }
for name,idol in favorite_idols.items():
    print(name.title()+"'s favorite idol is "+
          idol.title()+".")


