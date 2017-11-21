#5.4.1 检查特殊元素
requested_toppings=['mushrooms','greenpeppers','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping=='greenpeppers':
        print('Sorry, we are out of '+requested_topping+' now.')
    else:
        print('Addinig '+requested_topping.title()+'.')
print('\nFinished making your pizza!')