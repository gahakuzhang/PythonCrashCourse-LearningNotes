#9.1 creating and using a class 创建和使用类
#9.1.1 creating the dog class 创建dog类
#dogs.py
class Dog():
    """a simple attempt to model a dog"""
    def __init__(self,name,age):
        """initialize name and age attributes 初始化属性"""
        self.name=name
        self.age=age
    def sit(self):
        """simulate a dog sitting in response to a command"""
        print(self.name.title()+" is now sitting.")
    def roll_over(self):
        """simulate rolling over in response to a command"""
        print(self.name.title()+" rolled over!")
# 类中的函数称为方法 method
# __init__方法的第一个参数永远是self，表示创建的实例本身
# 因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身
# 有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，
# 但self不需要传，Python解释器自己会把实例变量传进去
# 以self为前缀的变量可供类中的所有方法使用
# self.name=name获取存储在形参name中的值，并将其存储到变量name中，该变量再被关联到当前的实例
# 这种可通过实例访问的变量（即self.name的name）称为属性 attribute

# 和普通的函数相比，在类中定义的函数只有一点不同：第一个参数永远是实例变量self，并且调用时不用传递该参数。
# 类的方法和普通函数没有什么区别，所以仍可以用默认参数、可变参数、关键字参数和命名关键字参数。

#9.1.2 making an instance from a class 根据类创建实例
# accessing attributes 访问属性
class Dog():
    """a simple attempt to model a dog"""
    def __init__(self,name,age):
        """initialize name and age attributes 初始化属性"""
        self.name=name
        self.age=age
    def sit(self):
        """simulate a dog sitting in response to a command"""
        print(self.name.title()+" is now sitting.")
    def roll_over(self):
        """simulate rolling over in response to a command"""
        print(self.name.title()+" rolled over!")

my_dog=Dog('willie',6)
print("My dog's name is "+my_dog.name.title()+".")
print("My dog is "+str(my_dog.age)+" years old.")
# my_dog.name 句点表示法，表示访问实例的属性，其中my_dog是实例，name是属性

# calling methods 调用方法
# class Dog():
#     --snip--
#
# my_dog=Dog('willie',6)
# my_dog.sit()
# my_dog.roll_over()

# creating multiple instances 创建多个实例
# class Dog():
#     --snip--
#
# my_dog=Dog('willie',6)
# your_dog=Dog('lucy',3)
# print("My dog's name is "+my_dog.name.title()+".")
# print("My dog is "+str(my_dog.age)+" years old.")
# my_dog.sit()
# print("\nYour dog's name is "+my_dog.name.title()+".")
# print("Your dog is "+str(your_dog.age)+" years old.")
# your_dog.sit()



# 9.2 working with classes and instances 使用类和实例
# 9.2.1 the car class
class Car():
    """模拟汽车"""
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make=make
        self.model=model
        self.year=year
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
my_new_car=Car('audi','a4','2016')
print(my_new_car.get_descriptive_name())
# self.make=make,第一个make是属性，第一个make是形参

#9.2.2 setting a default value for an attribute 为属性指定默认值
class Car():
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has "+str(self.odometer_reading)+" miles on it.")
my_new_car=Car('audi','a4','2016')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
# 调用__init__()创建新实例时，以属性的形式存储make model year,并创建一个初始值为0的属性odometer_reading

# 9.2.3 modifying attribute values 直接修改属性值
# class Car():
    #--snip--
my_new_car=Car('audi','a4','2016')
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading=23
my_new_car.read_odometer()
# line113,使用句点表示法直接访问并设置属性odometer_reading

# 9.2.3 modify an attribute's value through a method 通过方法修改属性值
class Car():
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has "+str(self.odometer_reading)+" miles on it.")
    def update_odometer(self,mileage):
        """将里程表读数设为指定值"""
        self.odometer_reading=mileage
my_new_car=Car('audi','a4','2016')
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()
# 也可以将mileage设置为__init__()的形参

# 直接将mileage设置成__init__()的形参
# 缺点是无法为odometer_reading属性设置初始值
# 上面一行的想法错误，见第5行和第18行。位置实参。
class Car():
    def __init__(self,make,model,year,mileage=0):
        """初始化描述汽车的属性"""
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=mileage
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has "+str(self.odometer_reading)+" miles on it.")
my_new_car=Car('audi','a4','2016',23)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

#
class Car():
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has "+str(self.odometer_reading)+" miles on it.")
    def update_odometer(self,mileage):
        """
        将里程表读数设为指定值
        禁止将里程表往回调
        """
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can't roll back an odometer!")

# incrementing an attibute's value through a method 通过方法对属性的值进行递增
class Car():
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has "+str(self.odometer_reading)+" miles on it.")
    def update_odometer(self,mileage):
        """将里程表读数设为指定值"""
        self.odometer_reading=mileage
    def increment_odometer(self,miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading+=miles
my_used_car=Car('subaru','outback','2013')
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()



# 9.3 Inheritance 继承
# 9.3.1 the __init()__ method for a child class 子类的方法
class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")
    def update_odometer(self,mileage):
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self,miles):
        self.odometer_reading+=miles

class ElctricCar(Car):
    def __init__(self,make,model,year):
        """初始化父类的属性"""
        super().__init__(make,model,year)
my_tesla=ElctricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
# 创建子类时，父类必须包含在当前文件中，位于子类之前。
# 定义子类时，()内包括父类的名称，class ElctricCar(Car):
# super()关联父类和子类
# super().__init__(make,model,year)调用父类的方法__init__()
# 父类parent class也被称为超类 superclass

# 9.3.3 define attributes and methods for the child class 为子类定义属性和方法
class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")
    def update_odometer(self,mileage):
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self,miles):
        self.odometer_reading+=miles

class ElctricCar(Car):
    def __init__(self,make,model,year):
        """初始化父类的属性,再初始化电动汽车特有的属性"""
        super().__init__(make,model,year)
        self.battery_size=70
    def describe_battery(self):
        print("This car has a "+str(self.battery_size)+"-kWh battery.")
my_tesla=ElctricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()


# 9.3.4 override methods from the parent class
# 在子类中定义一个方法，与父类中的方法同名，Python会只关注子类中定义的相应办法

# 9.3.5 instances as attributes 将实例用作属性
class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")
    def update_odometer(self,mileage):
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self,miles):
        self.odometer_reading+=miles

class Battery():
    """模拟电动汽车电瓶"""
    def __init__(self,battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size=battery_size
    def describe_battery(self):
        """打印电瓶容量"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """初始化父类的属性,再初始化电动汽车特有的属性"""
        super().__init__(make, model, year)
        self.battery=Battery()
my_tesla=ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
# self.battery=Battery()意为创建一个新的Battery实例（没有指定实参），并将该实例存储在属性self.battery
# my_tesla.battery.describe_battery() 在实例my_tesla中查找属性battery
# 并对存储在属性my_tesla.battery中的Battery实例调用方法describe_battery()
# 这样做不会导致ElectricCar中混乱不堪

# 9.3.5-2 instances as attributes 将实例用作属性
# 30行为Battery类添加一个报告续航里程的方法
class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")
    def update_odometer(self,mileage):
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self,miles):
        self.odometer_reading+=miles

class Battery():
    """模拟电动汽车电瓶"""
    def __init__(self,battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size=battery_size
    def describe_battery(self):
        """打印电瓶容量"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    def get_range(self):
        """打印电瓶的续航里程"""
        if self.battery_size==70:
            range=240
        if self.battery_size==85:
            range=270
        message="This car can go approximately "+str(range)
        message+=" miles on a full charge"
        print(message)
class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """初始化父类的属性,再初始化电动汽车特有的属性"""
        super().__init__(make, model, year)
        self.battery=Battery()
my_tesla=ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# 9.3.6 modelling real-world objects 模拟实物
# 从逻辑层面而不是语法层面解决问题
# 建模方法没有对错之分，只有效率高低之分


# 9.4 importing classes 导入类
# 9.4.1 import a single class
# 9.4.2 store multiple classes in a module
# 9.4.1和9.4.2详见子文件夹
from car import Car, ElectricCar
# 9.4.3 import multiple classes from a module 从一个模块导入多个类
from car import Car, ElectricCar
# 9.4.4 import an entire module导入整个模块
import car
# 9.4.5 import all classes from a module导入模块中所有类
from module_name import *
# 9.4.6 import a module into a module 在一个模块中导入另一个模块


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



# 9.6 styling classes 类编码风格
# 驼峰命名法：类名中每个单词首字母大写，不使用下划线
# 实例和模块用小写，单词之间使用下划线
