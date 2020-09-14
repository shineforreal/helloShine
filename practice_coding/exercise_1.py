#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math

"""
小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
"""
s1 = 72
s2 = 85
r = (s2 -s1)/s1*100
print(f"小明成绩提升了{r:.1f}%")
print("小明成绩提升了{0:.1f}%".format(r))
print("小明成绩提升了%.1f%%" %r)

"""
请用索引取出下面list的指定元素：
"""
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])
print(L[-1][-1])

'''
小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
用if-elif判断并打印结果：
'''
height = 1.55
weight = 44.5
bmi = weight/(height**2)
if bmi<18.5:
    print("过轻")
elif bmi>=18.5 and bmi<25:
    print("正常")
elif bmi>=25 and bmi<28:
    print("过重")
elif bmi>=28 and bmi<32:
    print("肥胖")
elif bmi>32:
    print("严重肥胖")

"""
请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：
"""
n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))


"""
请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax^2+bx+c=0的两个解。

提示：
计算平方根可以调用math.sqrt()函数：
"""
def quadratic(a,b,c):
    if b**2-4*a*c>=0:
        m = (math.sqrt(b**2-4*a*c)-b)/(2*a)
        n = (-math.sqrt(b**2-4*a*c)-b)/(2*a)
        return m,n
    else:
        print("无解")

   
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')


"""
以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
def product(x, y):
    return x * y
"""
def product(*x):
    if x == ():
        raise TypeError("没有输入参数")
    num = 1
    for i in x:
        num = i*num
    return num
# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')
    
"""
汉诺塔的移动可以用递归函数非常简单地实现。
请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法，例如：
还没有写出来
"""
def move(n):
    if n == 1:
        print("a-->c,")
    elif n == 2:
        print(r'''a-->b,
        a-->c,
        b--c>
        ''')
    else:
        move(n-1)
        move(1)

move(3)
