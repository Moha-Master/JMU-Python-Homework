import math as mt
def homework_1():
    print("请输入用电量：")
    w = float(input())
    if 200 >= w >= 0 :
        price = 0.5 * w
    elif 400>= w >200 :
        price = 100 + 0.55 * (w - 200)
    else :
        price = 100 + 0.55 * 200 + 0.8 * (w - 400)
    price = '%.2f' % price
    print ("用电量为" , price)

def homework_2():
    print("请输入x：")
    x = float(input())
    if 10 > x :
        y = mt.sin(x) + abs(x)
    elif 20 >= x >= 10 :
        y = mt.sqrt(3 * x) - 2
    else :
        y = 2 + 3 * x + mt.pow(x,2)
    y = '%.2f' % y
    print ("y=" , y)

def homework_3():
    print("请输入存款额（万元）：")
    cash = float(input())
    if 5 > cash :
        print("是普通客户")
    elif 30 > cash >= 5 :
        print("是银卡客户")
    elif 100 > cash >= 30 :
        print("是金卡客户")
    elif 300 > cash >= 100 :
        print("是白金客户")
    else :
        print("是黑金客户")

homework_1()
homework_2()
homework_3()
input("输入任意键退出作业演示")