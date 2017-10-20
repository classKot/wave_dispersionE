# wave_dispersionE
大学教科书上对于波浪的色散方程运用迭代的方式对波浪进行计算，若不借助计算机而进行人工计算需要迭代数十次甚至上百次，工作量巨大。本文将对其迭代方式进行改进以减少迭代次数。

参与变量：
T：周期(s)
h：水深(m)
g：重力加速度(固定取9.8m/s^2)
L：波长(m)

计算过程：
将波长L的初值设为(g*math.pow(T,2))/(2*math.pi)
通过色散方程迭代计算得出L值
L = ((g*math.pow(T,2))/(2*math.pi))*math.tanh((2*math.pi*h)/L)


教科书上的原方法(original method)： 


https://github.com/classKot/wave_dispersionE/blob/master/original/o_de_fig1.png

