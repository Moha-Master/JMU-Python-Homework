import os
libs = {"numpy", "re"};
 
try:
    for lib in libs:
        print("start install {0}".format(lib));
        os.system("pip install " + lib);
        print("{} install successful".format(lib));
    print("All Successful");
except:
    print("Failed SomeHow");

import re
import numpy as np

#打广告#
print("_______________________________________")
print("访问我的Github页面查看更多作业")
print("https://github.com/Moha-Master/JMU-Python-Homework")
print("_______________________________________")

#任务选择引导#
print("_______________________________________")
print("请选择要运行的任务")
print("输入1运行温度转换")
print("输入2运行表达式计算")
print("_______________________________________")
Choose = input()

#温度转换#
def TemperatureSwitch():
    print("请输入温度数值")
    TemperatureNumber = input()

    if not re.findall('^[0-9]+$', TemperatureNumber):
        print("////////////////////////////////////////////|")
        print("请不要输入除了数字以外的字符")
        print("////////////////////////////////////////////|")
        TemperatureSwitch()
    
    TemperatureNumber = eval(TemperatureNumber)
    TemperatureSign = input("请输入大写的温度单位")

    if TemperatureSign == "F":
        TemperatureNumber = (TemperatureNumber - 32) * 5 / 9
        print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|")
        print("转换后的温度值为{}摄氏度".format(TemperatureNumber))
        print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/|")

    elif TemperatureSign == "C":
        TemperatureNumber = (TemperatureNumber * 9 / 5) + 32
        print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|")
        print("转换后的温度为{}华氏度".format(TemperatureNumber))
        print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/|")

    else:
        print("////////////////////////////////////////////|")
        print("请输入正确的大写温度单位：C（摄氏度）或F（华氏度）")
        print("////////////////////////////////////////////|")
        TemperatureSwitch()
    print("_______________________________________")
    print("输入Q或q退出程序")
    print("_______________________________________")
    Quit = input()
    if not Quit == ("Q" or "q"):
        TemperatureSwitch()
    else:
        return

#表达式计算#
def Caculate():
    x = eval(input("请输入x："))
    y = eval(input("请输入y："))
    if y == 0:
        print("除数不可为0！请重新开始")
        Caculate()
    elif 3 * x - 1 <= 0:
        print("负数不可求对数！请重新开始")
        Caculate()
    else:
        result = np.log(3 * x - 1) / y
        print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|")
        print("结果为{}".format(result))
        print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/|")


#选择任务#
if Choose == "1":
    TemperatureSwitch()
elif Choose == "2":
    Caculate()
else:
    print("请输入正确选项！")

#暂停程序#
input()
