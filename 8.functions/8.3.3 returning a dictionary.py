#8.3.3 returning a dictionary 返回字典
#person['age']=age是添加键值对
def build_person(first_name,last_name,age=''):
    """返回一个字典，包含一个人的信息"""
    person={'first':first_name,'last':last_name}
    if age:
        person['age']=age
    return person
musician=build_person('jimi','hendeix',age=27)
print(musician)