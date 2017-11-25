#7.3 using a while loop with lists and dictionaries
#7.3.1 moving items from a list to another
#for循环中不应修改列表
unconfirmed_users=['alice','brian','candace']
confirmed_users=[]
while unconfirmed_users:
    current_user=unconfirmed_users.pop()
    print("Verifying user: "+current_user.title())
    confirmed_users.append(current_user)
print("\nThe following user have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
#while unconfirmed_users不断循环，直到unconfirmed_users变成空的
