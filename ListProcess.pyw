import tkinter as Tk

ls = [0,0,0,0,0,0]

#建立一个窗口
root = Tk.Tk()
root.title('Create & Process a List')
root.geometry('330x120')

#定义用于按钮调用的事件函数
def Refresh():
    Msg = Tk.Message(root,
                 width = 999,
                 text = ls,
                 font = ("微软雅黑","24"),
                 anchor = "w",
                 justify = "left")
    Msg.grid(column = 1,
         columnspan = 5,
         row = 1)

#向列表写入数值
def AddThings(): 
    ls[0] = 6
    ls[1] = 5
    ls[2] = 9
    ls[3] = 1
    ls[4] = 8
    ls[5] = 10
    Refresh()


#改变数值
def Change_2_to_16():
    ls[2] = 16
    Refresh()


#添加数值
def Add_2_20():
    ls.insert(2, 20)
    Refresh()


#删除数值
def Delete_1():
    ls.remove(1)
    Refresh()

#绘制窗口控件
bt1 = Tk.Button(root,
                text = "生成列表",
                command = Refresh)
bt1.grid(column = 1,
         columnspan = 1,
         row = 0)

bt2 = Tk.Button(root,
                text = "向列表写入数值",
                command = AddThings)
bt2.grid(column = 2,
         columnspan = 1,
         row = 0)

bt3 = Tk.Button(root,
                text = "改变数值",
                command = Change_2_to_16)
bt3.grid(column = 3,
         columnspan = 1,
         row = 0)

bt4 = Tk.Button(root,
                text = "添加数值",
                command = Add_2_20)
bt4.grid(column = 4,
         columnspan = 1,
         row = 0)

bt5 = Tk.Button(root,
                text = "删除数值",
                command = Delete_1)
bt5.grid(column = 5,
         columnspan = 1,
         row = 0)

Msg = Tk.Message(root,
                 width = 999,
                 text = "访问我的Github页面获取源码：https://github.com/Moha-Master/JMU-Python-Homework",
                 font = ("微软雅黑","9"),
                 anchor = "w",
                 justify = "left")
Msg.grid(column = 1,
         columnspan = 5,
         row = 2)
    
root.mainloop()
