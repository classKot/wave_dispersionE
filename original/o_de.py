import numpy as np
import matplotlib.pyplot as plt
import math

T = 10      # 波周期
h = 16      # 水深
g = 9.8     # 重力加速度
L = (g*math.pow(T,2))/(2*math.pi)       # 为波长赋初值
x = np.linspace(0,99,100)        # x变量数组（迭代次数）
y = np.linspace(0,99,100)        # y变量数组，每次迭代的新波长L的值
# 通过色散方程对波长L进行迭代
for i in range(100):
    L = ((g*math.pow(T,2))/(2*math.pi))*math.tanh((2*math.pi*h)/L)
    y[i] = L        # 将y变量数组用迭代得出的新的波长L值进行更新

print(L)
plt.axes()
plt.plot(x,y)       # 绘制x,y图像
plt.show()