# 6.1 dictionary使用{},使用键-值（key-value）存储
alien_0={'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])

# 6.2.1 访问字典中的值
alien_0={'color':'green','points':5}
new_points=alien_0['points']
print('You\'ve just earned '+str(new_points)+' points!')

# 6.2.2 添加key-value键-值对
alien_0={'color':'green','points':5}
print(alien_0)
alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)
# 6.2.2 key-value的排列顺序和添加顺序不同
# Python只关心key-vlaue的对应关系，不关心添加顺序

# 6.2.3 先定义1个空字典
alien_0={}
alien_0['color']='green'
alien_0['points']=5
print(alien_0)

# 6.2.4 修改value
alien_0={'color':'green'}
print('The alien is '+alien_0['color']+'.')
alien_0['color']='yellow'
print('The alien is now '+alien_0['color']+'.')
# pratice
idol_age={'nanamin':25,'rentan':13,'yuki':16}
print('This year rentan is '+str(idol_age['rentan'])+' years old.')
after_years=3
idol_age['rentan']=idol_age['rentan']+after_years
print('After '+str(after_years)+' years',
      'rentan will be '+str(idol_age['rentan'])+' years old.')

# 6.2.5 删除键-值对
idol_age={'nanamin':25,'rentan':13,'yuki':16,'kazumin':23}
del idol_age['kazumin']
print(idol_age)

# 6.2.6由类似对象组成的dictionary
# 为什么没有自动缩进？？？
# 最后的key-value后再加入一个逗号，为以后插入key-value做准备
favorite_idols={
    'me':'nanamin',
    'yc':'kazumin',
    'A':'nachan',
    'B':'maiyan',
    }
print("yc's favorite idol is "+
      str(favorite_idols['yc'].title())+".")

#6.3 遍历字典 looping through a dictionary
#6.3.1 遍历所有键值对
#6.3.1 使用items.()
#遍历字典时，键值对的返回顺序和存储顺序不同
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
    'a':'maiyan',
    'b':'erika',
    }
for name,idol in favorite_idols.items():
    print(name.title()+"'s favorite idol is "+
          idol.title()+".")

#6.3.2 遍历所有键
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
    'a':'maiyan',
    'b':'erika',
    }
iihito=['ghk','yc']
for name in favorite_idols.keys():
    print(name)
    if name in iihito:
        print("Hi "+name.title()+
              " , thanks for supporting "+
              favorite_idols[name].title()+".")

#6.3.3 按顺序遍历所有key
#注意sorted的位置
favorite_idols={
    'ghk':'nachan',
    'yc':'kazumin',
    'a':'maiyan',
    'b':'erika',
    }
for name in sorted(favorite_idols):
    print(name.title()+", thank you for supporting "
          +favorite_idols[name]+"!")

# 6.4 嵌套 nesting
# 将字典存储在列表中，或将列表作为值存在字典中
# 6.4.1 a list of dictionaries 字典列表
aliens=[]
# 创建30个绿色外星人
for alien_number in range(30):
    new_alien={'color':'green','points':5,'speed':'slow',}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)
print('...')
print("The total number of aliens: "+str(len(aliens)))

# 6.4.2 a list in a dictionary 在字典中存储列表
# pizza
pizza={
      'crust':'thick',
      'topping':['mushrooms','extra cheese'],
      }
print("You have ordered a "+pizza['crust']+'-crust pizza with the following toppings:')
for topping in pizza['topping']:
      print("\t"+topping)

#favorite_languages
favorite_languages={
    'jen':['python','ruby'],
    'sarah':'c',
    'edward':['ruby','go'],
    'phil':['python','haskell'],
    }
for name,languages in favorite_languages.items():
    print(name.title()+"'s favorite language is:")
    for language in languages:
        print("\t"+language)
#如果不使用第2个for循环，直接print(languages)，会出现类似['python', 'ruby']的结果

#6.4.3 a dictionary in a dictionary
fans={
    'ghk':{
        'age':25,
        'food':'ramen',
        'idol':'nachan',
    },
    'yc':{
        'age':27,
        'food':'fried chicken',
        'idol':'kazumin',
    },
}
for fansname,fansinfo in fans.items():
    print("fan's name: "+fansname)
    for faninfo in fansinfo:
        print(faninfo['food'])
#报错： print(faninfo['food']) TypeError: string indices must be integers
#最后两行改为print(fansinfo['food'])就没问题了

fans={
    'ghk':{
        'age':25,
        'food':'ramen',
        'idol':'nachan',
    },
    'yc':{
        'age':27,
        'food':'fried chicken',
        'idol':'kazumin',
    },
}
for fansname,fansinfo in fans.items():
    print("fan's name: "+fansname)
    for fansinfo_name,fansinfo_content in fansinfo:
        print(fansinfo_content)
#报错：for fansinfo_name,fansinfo_content in fansinfo:
# ValueError: too many values to unpack (expected 2)

fans={
    'ghk':{
        'age':25,
        'food':'ramen',
        'idol':'nachan',
    },
    'yc':{
        'age':27,
        'food':'fried chicken',
        'idol':'kazumin',
    },
}
for fansname,fansinfo in fans.items():
    print("fan's name: "+fansname)
    age=fansinfo['age']
    food=fansinfo['food']
    idol=fansinfo['idol']
    print(age)
    print(food.title())
    print(idol.title())
#未报错
#或者最后6行改为print(fansinfo['age'])...














