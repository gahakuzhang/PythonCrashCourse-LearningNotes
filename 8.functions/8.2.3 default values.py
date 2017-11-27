#8.2.3 default values 默认值
#函数调用时只有一个实参pet_name，然而Python仍将其视为位置实参，会自动关联到第一个形参
#因此需要将pet_name放到形参列表开头
def describe_pet(pet_name,animal_type="dog"):
    """显示宠物的信息"""
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")
describe_pet(pet_name="willie")
#describe_pet(animal_type="hamster",pet_name="harry")时Python将忽略默认值