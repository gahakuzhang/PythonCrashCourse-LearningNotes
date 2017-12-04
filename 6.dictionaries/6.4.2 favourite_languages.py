# 6.4.2 a list in a dictionary 在字典中存储列表
# favorite_languages
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