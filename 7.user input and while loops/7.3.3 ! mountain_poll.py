#7.3.3 filling a dictionary with user input
#mountains_poll
# responses[name]=response 添加键值对
responses={}
polling_active=True
while polling_active:
    name=input("\nWhat is your name? ")
    response=input("which mountain would you like to climb someday? ")
    responses[name]=response
    repeat=input("Would you like to let another person respond?(yes/no)")
    if repeat=='no':
        polling_active=False
print("\n--- Poll Results ---")
for name,response in responses.items():
    print(name+" would like to climb "+response+".")
