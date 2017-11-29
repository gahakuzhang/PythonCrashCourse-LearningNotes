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
# my_dog.name 句点表示法，表示访问实例的属性

# calling methods 调用方法
# class Dog():
#     --snip--
#
# my_dog=Dog('willie',6)
# my_dog.sit()
# my_dog.roll_over()

# creating multiple instances
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