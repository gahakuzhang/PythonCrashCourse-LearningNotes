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