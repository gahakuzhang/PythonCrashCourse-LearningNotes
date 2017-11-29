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