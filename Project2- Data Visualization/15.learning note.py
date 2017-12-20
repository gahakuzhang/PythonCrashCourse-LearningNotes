# 15.generate data 生成数据
# 15.2 plot a simple line graph 绘制简单的折线图
# mpl_squares.py
import matplotlib.pyplot as plt
squares=[1,4,9,16,25]
plt.plot(squares)
plt.show()
# 导入模块pyplot,指定别名plt
# 把列表squares传递给函数plot
# plt.show()打开matplotlib查看器

# 15.2.1 change the label type and graph thickness 修改标签文字和线条粗细
# mpl_squares.py
import matplotlib.pyplot as plt
squares=[1,4,9,16,25]
plt.plot(squares)
plt.show()

# 15.2.2 correct the plot 校正图形
# 15.2.3 plot and style individual points with scatter() 使用scatter()绘制散点图并设置其样式
# 15.2.4 plot a series of points with scatter() 使用scatter()绘制一系列点
# 15.2.5 calculate data automatically 自动计算数据
# 15.2.6 remove outlines from data points 删除数据点的轮廓
# 15.2.7 define custom colors 自定义颜色
# 15.2.8 use a colormap 使用颜色映射
# 15.2.9 save your plots automatically 自动保存数据

# 15.3 random walks 随机漫步