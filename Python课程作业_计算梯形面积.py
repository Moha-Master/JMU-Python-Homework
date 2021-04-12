from tkinter import *

#建立一个窗口
root = Tk()
root.config(background ="#FFFFFF") #设置背景颜色
root.geometry('300x600')
root.title('梯形面积计算器')

###绘制窗口控件###
topWidthMsg = Label(root,
                 text = "请输入上底高度",
                 bg =  "#FFFFFF",
                 font = ("微软雅黑",12),
                 fg = "#000000")
topWidthMsg.place(relx=0.3 ,rely=0)

underWidthMsg = Label(root,
                 text = "请输入下底高度",
                 bg =  "#FFFFFF",
                 font = ("微软雅黑",12),
                 fg = "#000000")
underWidthMsg.place(relx=0.3 ,rely=0.2)

HeightMsg = Label(root,
                 text = "请输入梯形高度",
                 bg =  "#FFFFFF",
                 font = ("微软雅黑",12),
                 fg = "#000000")
HeightMsg.place(relx=0.3 ,rely=0.4)

ResultMsg = Label(root,
                 text = "结果为",
                 bg =  "#FFFFFF",
                 font = ("微软雅黑",12),
                 fg = "#000000")
ResultMsg.place(relx=0.3 ,rely=0.6)

topWidthEntry = Entry(root,
                      bg =  "#FFFFFF",
                      font = ("微软雅黑",12),
                      fg = "#000000")
topWidthEntry.place(relx=0 ,rely=0.1 ,relwidth=1)

underWidthEntry = Entry(root,
                      bg =  "#FFFFFF",
                      font = ("微软雅黑",12),
                      fg = "#000000")
underWidthEntry.place(relx=0 ,rely=0.3 ,relwidth=1)

HeightEntry = Entry(root,
                      bg =  "#FFFFFF",
                      textvariable = "5",
                      font = ("微软雅黑",12),
                      fg = "#000000")
HeightEntry.place(relx=0 ,rely=0.5 ,relwidth=1)
###绘制窗口控件###

###运算过程###
def caculate():
    topW = topWidthEntry.get()
    underW = underWidthEntry.get()
    h = HeightEntry.get()
    if len(topWidthEntry.get()) == 0:
        ResultMsg1 = Text(root,
                                  bg =  "#FFFFFF",
                                  font = ("微软雅黑",12),
                                  fg = "#FF0000")
        ResultMsg1.place(relx=0 ,rely=0.7 ,relheight=0.1 ,relwidth=1)
        ResultMsg1.insert(END, "错误！请输入上底数值！")
    elif len(underWidthEntry.get()) == 0:
        ResultMsg1 = Text(root,
                                  bg =  "#FFFFFF",
                                  font = ("微软雅黑",12),
                                  fg = "#FF0000")
        ResultMsg1.place(relx=0 ,rely=0.7 ,relheight=0.1 ,relwidth=1)
        ResultMsg1.insert(END, "错误！请输入下底数值！")
    elif len(HeightEntry.get()) == 0:
        ResultMsg1 = Text(root,
                                  bg =  "#FFFFFF",
                                  font = ("微软雅黑",12),
                                  fg = "#FF0000")
        ResultMsg1.place(relx=0 ,rely=0.7 ,relheight=0.1 ,relwidth=1)
        ResultMsg1.insert(END, "错误！请输入梯形的高！")
    else:
        ResultMsg1 = Text(root,
                                  bg =  "#FFFFFF",
                                  font = ("微软雅黑",12),
                                  fg = "#000000")
        ResultMsg1.place(relx=0 ,rely=0.7 ,relheight=0.1 ,relwidth=1)
        result = (int(topW)+int(underW))*int(h)*0.5
        ResultMsg1.insert(END, result)
        topWidthEntry.delete(0, END)
        underWidthEntry.delete(0, END)
        HeightEntry.delete(0, END)
###运算过程###


###绘制一个按钮来执行运算###
Button = Button(root,
                text = "显示结果",
                bg = "#FFFFFF",
                fg = "#000000",
                command = caculate)
Button.place(relx=0 ,rely=0.8 ,relwidth=1 ,relheight=0.2)
###绘制一个按钮来执行运算###

root.mainloop()  #生成窗口


