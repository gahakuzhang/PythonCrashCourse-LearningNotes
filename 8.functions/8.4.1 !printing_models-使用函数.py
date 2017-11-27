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
