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
