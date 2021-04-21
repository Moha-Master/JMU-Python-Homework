import re

#打广告#
print("访问我的Github页面查看更多作业")
print("https://github.com/Moha-Master/JMU-Python-Homework")

#任务选择引导#
print("请选择要运行的任务")
print("输入1运行温度转换")
print("输入2运行水仙花数输出")
print("输入3运行素数输出")
Chopse = input()

#温度转换#
def TemperatureSwitch():
    TemperatureNumber = input("输入温度的数值")

    if not re.findall('^[0-9]+$', TemperatureNumber):
        print("请不要输入除了数字以外的字符")
        TemperatureSwitch()
    
    TemperatureNumber = eval(TemperatureNumber)

    TemperatureSign = input("请输入大写的温度单位")

    if TemperatureSign == "F":
        TemperatureNumber = (TemperatureNumber - 32) * 5 / 9
        print("转换后的温度值为{}摄氏度".format(TemperatureNumber))

    elif TemperatureSign == "C":
        TemperatureNumber = (TemperatureNumber * 9 / 5) + 32
        print("转换后的温度为{}华氏度".format(TemperatureNumber))

    else:
        print("请输入正确的大写温度单位：C（摄氏度）或F（华氏度）")
        TemperatureSwitch()
    print("输入Q或q退出程序")
    Quit = input()
    if not Quit == ("Q" or "q"):
        TemperatureSwitch()
    else:
        return

#水仙花数问题#
def FlowerQuestion():
    for First in range(1,9):
        for Second in range(0,9):
            for Third in range(0,9):
                if First**3 + Second**3 + Third**3 == First*100 + Second*10 + Third:
                    Num = First*100 + Second*10 + Third
                    print ("水仙花数为：{}".format(Num))

#求素数#
def SillyNumber():
    x,y = 0,0
    for Number in range(100,150):
        for DivNumber in range(2,Number):
            if Number%DivNumber == 0:
                x += Number
                y += 1
                print("{}是素数".format(Number))
                break
    print("共有{}个素数，和为{}".format(y,x))

#选择任务#
if Choose == "1":
    TemperatureSwitch()
elif Choose == "2":
    FlowerQuestion()
elif Choose == "3":
    SillyNumber()
else:
    print("请输入正确选项！")

#暂停程序#
input()