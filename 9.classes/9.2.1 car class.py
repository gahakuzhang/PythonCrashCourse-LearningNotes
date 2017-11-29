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