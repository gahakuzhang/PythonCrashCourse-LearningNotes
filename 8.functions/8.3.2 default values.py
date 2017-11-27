#将middle_name指定为默认值：空字符串，并移动到形参列表的末尾？？？
#Python将非空字符串解读为True，如果函数调用中提供了middle name，if middle_name将为True
#未提供middle name时，middle_name为空字符串，if测试无法通过，执行else代码块
#如果要指定middle·name，必须确保其是最后一个实参，这样python才能正确地将位置实参关联到形参
def get_formatted_name(first_name,last_name,middle_name=''):
    """返回整洁的姓名"""
    if middle_name:
        full_name=first_name+" "+middle_name+" "+last_name
    else:
        full_name=first_name+" "+last_name
    return full_name.title()
musician=get_formatted_name('john','lee','nooker')
print(musician)
musician=get_formatted_name('hashimoto','nanami')
print(musician)
