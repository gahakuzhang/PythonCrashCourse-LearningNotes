# 6.4.1 a list of dictionaries 字典列表
aliens=[]
# 创建30个绿色外星人
for alien_number in range(30):
    new_alien={'color':'green','points':5,'speed':'slow',}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)
print('...')
print("The total number of aliens: "+str(len(aliens)))