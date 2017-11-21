#4.4.1 Slicing a list 切片
idols=['nanamin','miona','nachan','maiyan','rentan','yuki']
print(idols[1:4]) #从第2个元素打印到第4个元素，即['miona', 'nachan', 'maiyan']。4意味着终止于4
print(idols[:4]) #从头打印到第4个元素，['nanamin', 'miona', 'nachan', 'maiyan']
print(idols[2:]) #从第3个打印到最后，['nachan', 'maiyan', 'rentan', 'yuki']
print(idols[-2:]) #从倒数第2个打印到最后，['rentan', 'yuki']
