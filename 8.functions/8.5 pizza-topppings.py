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