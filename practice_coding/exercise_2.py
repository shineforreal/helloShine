import random

'''

#保留几位小数
f = float(input("请输入华氏温度："))
c = (f-32)/1.8
print("%.2f华氏度 = %.2f摄氏度" %(f,c))
print(f"{f:.2f}华氏度 = {c:.2f}摄氏度") #第一个f是忽略里面的**

#输入圆的半径计算计算周长和面积。
def Circumference(radius):
    return 2*π*radius
    
def Circular_area(radius):
    return π*radius**2

π = 3.1415926
a = float(input("请输入圆的半径："))
print("%f为半径的圆，周长为:%f" % (a,Circumference(a)))
print("%f为半径的圆，面积为：%f" % (a,Circular_area(a)))


#练习3：输入年份判断是不是闰年。
def LeapYear(year):
    if year%400 == 0: #注意要用and 不要用&
        return True
    elif year%100 !=0 and year%4 == 0:
        return True
    else:
        return False

year = int(input("输入年份："))
print(LeapYear(year))


"""
分段函数求值

        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)

Version: 0.1
Author: 骆昊
"""
def f(x):
    result = 0
    if x>1:
        result = 3*x -5
    elif x>=-1 and x<=1:
        result = x+2
    else:
        result = 5*x + 3
    return result

x = 200.1
y = f(x)
print("f(%.1f) = %.1f" %(x,f(x)))
print(f"f({x:.2f}) = {y:.2f}") #这种就不要写%了


#英制单位英寸与公制单位厘米互换。
lenth = float(input("请输入长度："))
print("%f英寸 = %f厘米" %(lenth,lenth*2.54))
print("%f厘米 = %f英寸" %(lenth,lenth*0.3937008))


#### 练习3：输入三条边长，如果能构成三角形就计算周长和面积。
def tangle(a,b,c):
    if(a>0 and b>0 and c> 0 and a+b>c and b+c>a and a+c>b):
        if(max(a,b,c)==a):
            pass
        elif(max(a,b,c)==b):
            tmp = a
            a = b
            b = tmp
        else:
            tmp = c
            a = c
            c =tmp
        print("边长为%f,%f,%f的三角形，面积为：%f" %(a,b,c,1/4*(4*a**2*b**2-(a**2+b**2-c**2)**2)**0.5))
    else:
        print("无法构成三角形形！") 

tangle(1,2.5,3)


#练习3：打印如下所示的三角形图案。
for i in range(1,6):
    print(i*'*')

for i in range(1,6):
    print((5-i)*" ",i*'*')

for i in range(1,6):
    print((5-i)*" ",(i*2+1)*'*')


#寻找**水仙花数**。 
#**说明**:水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，它是一个3位数，该数字每个位上数字的立方之和正好等于它本身，例如：$1^3 + 5^3+ 3^3=153$。
def Narcissistic_num(i):
    if ((i//100)**3 + ((i-(i//100)*100)//10)**3 + (i%10)**3 ) == i:
        print("%d 是水仙花数" %(i))

for i in range(100,1000):
    if ((i//100)**3 + ((i-(i//100)*100)//10)**3 + (i%10)**3 ) == i:
        print("%d 是水仙花数" %(i))
Narcissistic_num(153)


#数字反转
def reversal(n):
    tmp = n
    result = 0
    while tmp//10!=0:
        result = result * 10 +tmp%10
        tmp = tmp//10
    result = result*10 + tmp%10
    return result

print(reversal(12305670))

num = 12434056780
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)      


#公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
def hundred_y_h_c():
    for i in range(0,21):
        for j in range(0,34):
            if (100 - 5*i - 3*j)>=0 and i +j +(100 - 5*i - 3*j)*3 == 100:
                print("%d只公鸡，%d只母鸡，%d只小鸡" % (i,j,(100 - 5*i - 3*j)*3))
hundred_y_h_c()

CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。
该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。
简单的规则是：玩家第一次摇骰子如果摇出了7点或11点，玩家胜；
玩家第一次如果摇出2点、3点或12点，庄家胜；
其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；
如果玩家摇出了第一次摇的点数，玩家胜；其他点数，玩家继续要骰子，直到分出胜负。


count = 1
while True:
    x = random.randint(1,6)
    y = random.randint(1,6)
    print("现在是第%d轮，这一轮的筛子是%d,%d" %(count,x,y))
    if count == 1:
        if x+y in (7,11):
            print("玩家胜！")
            break
        elif x+y in (2,3,12):
            print("庄家胜！")
            break
        first = x+y
    else:
        if x+y == 7:
            print("庄家胜！")
            break
        elif x+y ==  first:
            print("玩家胜！")
            break
    count +=1
'''
#生成**斐波那契数列**的前20个数
def Fibonacci1(n):
    if n<=0:
        print("wrong numbers!")
        return
    if n == 1:
        list1 = [1]
    elif n == 2:
        list1.append(1)
    else:
        list1.append(Fibonacci(n-1)+Fibonacci(n-2))
    return list1
    
def Fibonacci(n):
    if n<=0:
        print("wrong numbers!")
        return
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return (Fibonacci(n-1)+Fibonacci(n-2))


def Fibonacci_list(m):
    list1 = []
    for i in range(1,m+1):
        list1.append(Fibonacci(i))
        print ('%d ' %(Fibonacci(i)))
    return list1

print(Fibonacci_list(20))

a = 0
b = 1
for _ in range(20):
    a, b = b, a + b
    print(a, end=' ')
a = 0
b = 1


#找出10000以内的**完美数**
#完美数又称为完全数或完备数，它的所有的真因子（即除了自身以外的因子）的和（即因子函数）恰好等于它本身。
#例如：6（$6=1+2+3$）和28（$28=1+2+4+7+14$）就是完美数。完美数有很多神奇的特性，有兴趣的可以自行了解。
def perfect():
    pass

#输出**100以内所有的素数**。素数指的是只能被1和自身整除的正整数（不包括1）。
def prime():
    pass
