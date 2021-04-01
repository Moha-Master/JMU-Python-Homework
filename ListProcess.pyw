import tkinter as Tk

ls = [0,0,0,0,0,0]

#建立一个窗口
root = Tk.Tk()
root.title('Create & Process a List')
root.geometry('900x600')

#定义用于按钮调用的事件函数
def BornList():
    global Msg
    Msg = Tk.Message(root,
                 width = 999,
                 text = ls,
                 font = ("微软雅黑","24"),
                 anchor = "w",
                 justify = "left")
    Msg.grid(column = 1,
         columnspan = 5,
         row = 1)
    
def Refresh():
    global Msg
    Msg.grid_forget()
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


#改变数值
def Change_2_to_16():
    ls[2] = 16


#添加数值
def Add_2_20():
    ls.insert(2, 20)


#删除数值
def Delete_1():
    del ls[1]


#删除更多数值
def Delete_1_3():
    del ls[1:3]

#判断是否存在某值
def Ifelse():
    if "0" in ls:
        Msg1 = Tk.Message(root,
                 width = 999,
                 text = "确实",
                 font = ("微软雅黑","24"),
                 anchor = "w",
                 justify = "left")
        Msg1.grid(column = 1,
                  columnspan = 5,
                  row = 2)
    else:
        Msg1 = Tk.Message(root,
                 width = 999,
                 text = "瞎说",
                 font = ("微软雅黑","24"),
                 anchor = "w",
                 justify = "left")
        Msg1.grid(column = 1,
                  columnspan = 5,
                  row = 2)

#再添加个项目
def NewItem():
    ls.insert(2, 0)

#返回索引
def Return():
    id = ls.index(0)
    Msg2 = Tk.Message(root,
                      width = 999,
                      text = id,
                      font = ("微软雅黑","24"),
                      anchor = "w",
                      justify = "left")
    Msg2.grid(column = 1,
              columnspan = 5,
              row = 3)

#计算长度
def CaculateLenth():
    Lenth = len(ls)
    Msg3 = Tk.Message(root,
                 width = 999,
                 text = Lenth,
                 font = ("微软雅黑","24"),
                 anchor = "w",
                 justify = "left")
    Msg3.grid(column = 1,
              columnspan = 5,
              row = 4)

#返回极值
def Return_Max_Min():
    Max = max(ls)
    Min = min(ls)
    Msg4 = Tk.Message(root,
                 width = 999,
                 text = Max,
                 font = ("微软雅黑","24"),
                 anchor = "w",
                 justify = "left")
    Msg4.grid(column = 1,
              columnspan = 3,
              row = 5)
    Msg5 = Tk.Message(root,
                 width = 999,
                 text = Min,
                 font = ("微软雅黑","24"),
                 anchor = "w",
                 justify = "left")
    Msg5.grid(column = 4,
              columnspan = 3,
              row = 5)

#逆序输出
def Back():
    Back = ls[::-1]
    Msg = Tk.Message(root,
                 width = 999,
                 text = Back,
                 font = ("微软雅黑","24"),
                 anchor = "w",
                 justify = "left")
    Msg.grid(column = 1,
         columnspan = 5,
         row = 1)

#升降排序
def Up():
    ls.sort()

def Down():
    ls.sort(reverse=True)

#绘制窗口控件
bt0 = Tk.Button(root,
                text = "刷新显示",
                command = Refresh)
bt0.grid(column = 1,
         columnspan = 1,
         row = 0)

bt1 = Tk.Button(root,
                text = "生成列表",
                command = BornList)
bt1.grid(column = 2,
         columnspan = 1,
         row = 0)

bt2 = Tk.Button(root,
                text = "写入数值",
                command = AddThings)
bt2.grid(column = 3,
         columnspan = 1,
         row = 0)

bt3 = Tk.Button(root,
                text = "改变数值",
                command = Change_2_to_16)
bt3.grid(column = 4,
         columnspan = 1,
         row = 0)

bt4 = Tk.Button(root,
                text = "添加数值",
                command = Add_2_20)
bt4.grid(column = 5,
         columnspan = 1,
         row = 0)

bt5 = Tk.Button(root,
                text = "删除数值",
                command = Delete_1)
bt5.grid(column = 6,
         columnspan = 1,
         row = 0)

bt6 = Tk.Button(root,
                text = "再删几个",
                command = Delete_1_3)
bt6.grid(column = 7,
         columnspan = 1,
         row = 0)

bt7 = Tk.Button(root,
                text = "存在判断",
                command = Ifelse)
bt7.grid(column = 8,
         columnspan = 1,
         row = 0)

bt8 = Tk.Button(root,
                text = "再加元素",
                command = NewItem)
bt8.grid(column = 9,
         columnspan = 1,
         row = 0)

bt9 = Tk.Button(root,
                text = "返回索引",
                command = Return)
bt9.grid(column = 10,
         columnspan = 1,
         row = 0)

bt10 = Tk.Button(root,
                text = "计算长度",
                command = CaculateLenth)
bt10.grid(column = 11,
         columnspan = 1,
         row = 0)

bt11 = Tk.Button(root,
                text = "返回极值",
                command = Return_Max_Min)
bt11.grid(column = 12,
         columnspan = 1,
         row = 0)

bt12 = Tk.Button(root,
                text = "逆序输出",
                command = Back)
bt12.grid(column = 13,
         columnspan = 1,
         row = 0)

bt13 = Tk.Button(root,
                text = "上升排序",
                command = Up)
bt13.grid(column = 14,
         columnspan = 1,
         row = 0)

bt14 = Tk.Button(root,
                text = "下降排序",
                command = Down)
bt14.grid(column = 15,
         columnspan = 1,
         row = 0)

root.mainloop()
