#8.1 defining a function
#greeter
def greet_user():
    """显示简单的问候语"""
    print("Hello!")
greet_user()

#8.1.1 passing information to a function
#8.1.2 arguments实参 and parameters形参
#username是形参，'jesse'是实参，实参是调用函数时传递给函数的信息
def greet_user(username):
    """显示简单的问候语"""
    print("Hello!"+username.title()+"!")
greet_user('jesse')

#8.2 passing arguments 传递实参
#8.2.1 positonal arguments 位置实参
#基于实参的顺序
#pets.py
def describe_pet(animal_type,pet_name):
    """显示宠物的信息"""
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")
describe_pet("hamster","harry")
#可以调用函数多次，例如
#describe_pet("hamster","harry")
#describe_pet("dog","willie")

#8.2.2 keyword arguments 关键字实参
def describe_pet(animal_type,pet_name):
    """显示宠物的信息"""
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")
describe_pet(animal_type="hamster",pet_name="harry")
#在实参中将名称和值对应

#8.2.3 default values 默认值
#函数调用时只有一个实参pet_name，然而Python仍将其视为位置实参，会自动关联到第一个形参
#因此需要将pet_name放到形参列表开头
def describe_pet(pet_name,animal_type="dog"):
    """显示宠物的信息"""
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")
describe_pet(pet_name="willie")
#describe_pet(animal_type="hamster",pet_name="harry")时Python将忽略默认值

#8.2.4 equivalent function calls 等效的函数调用
def describe_pet(pet_name,animal_name='dog'):
# 以下调用等效
describe_pet('harry','hamster')
describe_pet(pet_name="harry",animal_type="hamster")
describe_pet(animal_type="hamster",pet_name="harry")

#8.2.5 avoiding argument errors避免实参错误
#实参多于或少于形参时，将出现实参不匹配错误


#8.3 return values 返回值
#8.3.1 ruturning a simple value返回简单值
#formatted_name.py
def get_formatted_name(first_name,last_name):
    """返回整洁的姓名"""
    full_name=first_name+" "+last_name
    return full_name.title()
musician=get_formatted_name('hashimoto','nanami')
print(musician)
#调用返回值得函数时，需要提供一个变量，用于储存返回的值

#8.3.2 making an argument optional
def get_formatted_name(first_name,middle_name,last_name):
    """返回整洁的姓名"""
    full_name=first_name+" "+middle_name+" "+last_name
    return full_name.title()
musician=get_formatted_name('john','lee','nooker')
print(musician)
#将middle_name指定为默认值：空字符串，并移动到形参列表的末尾？？？
#Python将非空字符串解读为True，如果函数调用中提供了middle name，if middle_name将为True
#未提供middle name时，middle_name为空字符串，if测试无法通过，执行else代码块
#如果要指定middle name，必须确保其是最后一个实参，这样python才能正确地将位置实参关联到形参
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

#8.3.3 returning a dictionary 返回字典
#函数可返回任何类型的值，包括列表、字典等
#person.py
def build_person(first_name,last_name):
    """返回一个字典，包含一个人的信息"""
    person={'first':first_name,'last':last_name}
    return person
musician=build_person('jimi','hendeix')
print(musician)

#person['age']=age是添加键值对
def build_person(first_name,last_name,age=''):
    """返回一个字典，包含一个人的信息"""
    person={'first':first_name,'last':last_name}
    if age:
        person['age']=age
    return person
musician=build_person('jimi','hendeix',age=27)
print(musician)

#8.3.4 using a function with a while loop结合使用函数和while循环
#将用户输入值作为实参
def get_formatted_name(first_name,last_name):
    """返回整洁的姓名"""
    full_name=first_name+" "+last_name
    return full_name.title()
#这是一个无限循环
while True:
    print("\nPlease tell me your name:")
    f_name=input("First name: ")
    l_name=input("Last name: ")
    formatted_name=get_formatted_name(f_name,l_name)
    print("\nHello, "+formatted_name+"!")

#使用break退出
#将用户输入值作为实参
def get_formatted_name(first_name,last_name):
    """返回整洁的姓名"""
    full_name=first_name+" "+last_name
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name=input("First name: ")
    if f_name=='q':
        break
    l_name=input("Last name: ")
    if l_name=='q':
        break
    formatted_name=get_formatted_name(f_name,l_name)
    print("\nHello, "+formatted_name+"!")


#8.4 passing a list 传递列表
def greet_users(names):
    """向列表中的每一位用户发出简单的问候"""
    for name in names:
        msg="Hello, "+name.title()+"!"
        print(msg)
usernames=['nanamin','miona','nachan']
greet_users(usernames)

#8.4.1 modifying a list in a function 在函数中修改列表
#printing_models.py
#不使用函数
#打印每个设计后，将其移动到completed_models中
unprinted_designs=['iphone case','robot pendant','dodecahedron']
completed_models=[]
while unprinted_designs:
    current_design=unprinted_designs.pop()
    print("Printing model: "+current_design)
    completed_models.append(current_design)
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

#使用函数
#第一个函数负责处理打印设计，第二个函数将概述打印了哪些设计
#每个函数只负责一项具体工作。程序执行的任务太多时，可以尝试将函数划分到多个函数中
def print_models(unprinted_designs,completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)
def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
#以下为主程序，更加清晰
unprinted_designs=['iphone case','robot pendant','dodecahedron']
completed_models=[]
print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)

#8.4.2 preventing a function from modifying a list
#向函数传递列表的切片
#function_name(list_name[:])
#例如print_models(unprinted_designs[:],completed_models)
#函数所做的修改不会影响unprinted_designs
#一般还是使用原本而非副本，节约时间和内存


#8.5 passing on arbitraty number of arguments 传递任意数量的实参
#pizza.py
def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')
#*toppnigs 是生成一个名为toppings的空元组，并将所有值封装入该元组
# 结果为('pepperoni',)，('mushrooms', 'green peppers', 'extra cheese')

#对配料列表进行遍历
def make_pizza(*toppings):
    """概述所要制作的pizza"""
    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print("-"+topping)
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')

#8.5.1 mixing positional and arbitrary arguments 结合使用位置实参和任意数量实参
#必须将接纳任意数量实参的形参放在最后
#Python先匹配位置实参和关键字实参，再将余下所有实参放到最后一个形参中
#本例中，size必须放在*toppings前面
def make_pizza(size,*toppings):
    """概述所要制作的pizza"""
    print("\nMaking a "+str(size)+"-inch pizza with the following toppings: ")
    for topping in toppings:
        print("-"+topping)
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')

#8.5.2 using arbitrary keyword arguments 使用任意数量的关键字实参
#user_profile.py
def build_profile(first,last,**user_info):
    """创建一个字典，包含我们所知道的用户的一切"""
    profile={}
    profile['first_name']=first
    profile['last_name']=last
    for key,value in user_info.items():
        profile[key]=value
    return profile
user_profile=build_profile('albert','einstein',
                           location='princeton',
                           field='physics')
print(user_profile)
#返回字典

#8.6 storing functions in modules 将函数储存在模块中
#8.6.1 importing an entire module
#module是.py文件
#pizza.py
def make_pizza(size,*toppings):
    """概述所要制作的pizza"""
    print("\nMaking a "+str(size)+"-inch pizza with the following toppings: ")
    for topping in toppings:
        print("-"+topping)
#8.6.1 making_pizzas.py
import pizza
pizza.make_pizza(16,'pepperoni')
pizza.make_pizza(12,'mushrooms','green peppers','extra cheese')
#使用import语句导入module_name，并使用module_name.function_name()，句点表示法
#注意import module_name后不加py
#pizza.py和making_pizzas.py必须在同一个文件夹

#8.6.2 importing specific functions 导入特定的函数
#导入模块中的特定函数
#from module_name import function_name
#from module_name import function_0,function_1,fucntion_2
#以前面的making_pizza.py为例
#pizza.py和making_pizzas.py必须在同一个文件夹
from pizza import make_pizza
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')
#调用函数时无需再使用"."，调用时直接指定函数的名称

#8.6.3 using as to give a function an alias 使用as为函数指定别名
#from module_name import function_name as fn
#避免名称冲突或者函数名称太长
from pizza import make_pizza as mp
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')

#8.6.4 using as to give a module an alias 使用as为模块指定别名
#import module_name as mn
import pizza as p
p.make_pizza(16,'pepperoni')
p.make_pizza(12,'mushrooms','green peppers','extra cheese')

#8.6.5 importing all functions in a module 导入函数中所有的函数
#使用*可导入模块中的所有函数
#from module_name import *
#由于导入了所有函数，不需要使用句点表示法，直接通过名称调用每个函数
#最好不要使用这种形式，出现名称相同的变量或函数时，有可能覆盖变量
#最佳做法：只导入需要的函数；或导入整个模块并使用句点表示法
from pizza import *
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')


#8.7 styling functions 函数编写指南
#1.每个函数都要有阐述功能的注释，采用文档字符串格式
#2.给形参指定默认值时，等号两边不要有空格
#def function_name(parameter_0,parameter_1='default value')
#函数调用中的关键字实参，等号两边不要有空格
#function_name(value_0,parameter_1='value')
#3.形参很多时，如下表示：形参列表和函数体区分
def function_name(
        parameter_0,parameter_1,
        parameter_2,parameter_3,):
    function_body
#4.多个函数之间可以用空行隔开
#5.import放在文件开头


#8.8 summary


