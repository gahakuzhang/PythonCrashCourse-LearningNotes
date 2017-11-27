#8.4.1 modifying a list in a function 在函数中修改列表
#printing_models.py
#不使用函数
#打印每个设计后，将其移动到completed_models中
unprinted_designs=['iphone case','robot pendant','dodecahedron']
completed_models=[]
while unprinted_designs:
    current_design=unprinted_designs.pop()
    print("Printing model: "+current_design)
    completed_models.append(current_design)
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)