#5.4.3 使用多个列表
avaible_toppings=['mushrooms','olives','green peppers',
                  'pepperoni','pineapple','extra cheese']
requested_toppings=['mushrooms','french fries','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in avaible_toppings:
        print('Adding '+requested_topping+'.')
    else:
        print('Sorry, we don\'t have '+requested_topping+'.')
print('\nFinished making your pizza!')
