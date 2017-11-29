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