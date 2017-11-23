#6.4.2 a list in a dictionary
#pizza
pizza={
      'crust':'thick',
      'topping':['mushrooms','extra cheese'],
      }
print("You have ordered a "+pizza['crust']+'-crust pizza with the following toppings:')
for topping in pizza['topping']:
      print("\t"+topping)