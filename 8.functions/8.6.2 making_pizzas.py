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

