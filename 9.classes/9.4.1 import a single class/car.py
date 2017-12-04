"""一个表示汽车的类"""

class Car():

    def __init__(self,make,model,year):
        """汽车属性"""
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        """返回整洁的描述性名称"""
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name.title()

    def read_odometer(self):
        """打印汽车里程"""
        print("This car has "+str(self.odometer_reading)+" miles on it.")

    def update_odometer(self,mileage):
        """更改里程但禁止回拨"""
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        """将里程表增加指定的量"""
        self.odometer_reading+=miles

