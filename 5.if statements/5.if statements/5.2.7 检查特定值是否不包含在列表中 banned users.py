#5.2.7检查特定值是否在列表中 not in
banned_users=['nanamin','miona','nachan']
user='maiyan'
if user not in banned_users:
    print(user.title()+', you can reponse if you wish')