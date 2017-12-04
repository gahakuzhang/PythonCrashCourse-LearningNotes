# 9.5 the Python standard library Python标准库
# 标准库是一组模块，可以使用其中的任何函数和类
# 字典不记录添加键值对的顺序
# 可使用模块collections中的OrderedDict类
# 该类的行为和字典几乎相同，区别在于记录了键值对的顺序
from collections import OrderedDict
favorite_languages=OrderedDict()

favorite_languages['jen']='python'
favorite_languages['sarah']='c'
favorite_languages['edward']='ruby'
favorite_languages['phil']='python'

for name,language in favorite_languages.items():
    print(name.title() + "'s favorite language is:"+
          language.title()+'.')
# OrderedDict() 不使用花括号，而是利用OrderedDict()来创建一个有序的空字典