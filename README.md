# wave_dispersionE
大学教科书上对于波浪的色散方程运用迭代的方式对波浪进行计算，若不借助计算机而进行人工计算需要迭代数十次甚至上百次，工作量巨大。本文将对其迭代方式进行改进以减少迭代次数。

参与变量
--------------------------
T：周期(s)\
h：水深(m)\
g：重力加速度(固定取9.8m/s^2)\
L：波长(m)

计算过程
--------------------------------
将波长L的初值设为(g*math.pow(T,2))/(2*math.pi)\
通过色散方程迭代计算得出L值\
L = ((g*math.pow(T,2))/(2*math.pi))*math.tanh((2*math.pi*h)/L)


教科书上的原方法(original method)
=========================================
T = 10\
h = 16\
最后L的值为：111.71424163460395

而y数组为：[  88.58992481  126.75087613  102.96998517  117.20746338  108.41292831
  113.75511674  110.47368259  112.47626916  111.24912297  111.9992484
  111.54001643  111.82090168  111.64900305  111.75416663  111.68981633
  111.7291876   111.70509727  111.71983684  111.71081822  111.7163363
  111.71296001  111.71502581  111.71376183  111.71453521  111.71406201
  111.71435154  111.71417439  111.71428278  111.71421646  111.71425704
  111.71423221  111.7142474   111.71423811  111.71424379  111.71424031
  111.71424244  111.71424114  111.71424194  111.71424145  111.71424175
  111.71424157  111.71424168  111.71424161  111.71424165  111.71424162
  111.71424164  111.71424163  111.71424164  111.71424163  111.71424164
  111.71424163  111.71424163  111.71424163  111.71424163  111.71424163
  111.71424163  111.71424163  111.71424163  111.71424163  111.71424163
  111.71424163  111.71424163  111.71424163  111.71424163  111.71424163
  111.71424163  111.71424163  111.71424163  111.71424163  111.71424163
  111.71424163  111.71424163  111.71424163  111.71424163  111.71424163
  111.71424163  111.71424163  111.71424163  111.71424163  111.71424163
  111.71424163  111.71424163  111.71424163  111.71424163  111.71424163
  111.71424163  111.71424163  111.71424163  111.71424163  111.71424163
  111.71424163  111.71424163  111.71424163  111.71424163  111.71424163
  111.71424163  111.71424163  111.71424163  111.71424163  111.71424163]
  
  若要精确度在小数点后两位的话，需要至少迭代19次

![error](https://github.com/classKot/wave_dispersionE/blob/master/original/o_de_fig1.png?raw=true)

改进后方法
======================
T = 10\
h = 16\
最后L的值为：111.71424163460395

而迭代数组为：[ 122.28088452  113.87673222  112.13850461  111.79675437  111.73026162
  111.7173509   111.71484506  111.71435874  111.71426436  111.71424605
  111.71424249  111.7142418   111.71424167  111.71424164  111.71424164
  111.71424163  111.71424163  111.71424163  111.71424163  111.71424163
  111.71424163  111.71424163  111.71424163  111.71424163  111.71424163
  111.71424163  111.71424163  111.71424163  111.71424163  111.71424163
  111.71424163  111.71424163  111.71424163  111.71424163  111.71424163
  111.71424163  111.71424163  111.71424163  111.71424163  111.71424163
  111.71424163  111.71424163  111.71424163  111.71424163  111.71424163
  111.71424163  111.71424163  111.71424163  111.71424163  111.71424163
  111.71424163  111.71424163  111.71424163  111.71424163  111.71424163
  111.71424163  111.71424163  111.71424163  111.71424163  111.71424163
  111.71424163  111.71424163  111.71424163  111.71424163  111.71424163
  111.71424163  111.71424163  111.71424163  111.71424163  111.71424163
  111.71424163  111.71424163  111.71424163  111.71424163  111.71424163
  111.71424163  111.71424163  111.71424163  111.71424163  111.71424163
  111.71424163  111.71424163  111.71424163  111.71424163  111.71424163
  111.71424163  111.71424163  111.71424163  111.71424163  111.71424163
  111.71424163  111.71424163  111.71424163  111.71424163  111.71424163
  111.71424163  111.71424163  111.71424163  111.71424163  111.71424163]
  
  若要精确度在小数点后两位的话，只需要迭代7次，大大减少工作量

