print("欢迎访问我的Github空间")
print("https://github.com/Moha-Master")

from itertools import chain

#小写转大写#
def Lower_to_Upper():
    #读取源文件#
    Lower = open("Lower.txt","r")
    Upper_Letter = Lower.read()
    Lower.close()
    print("已读取Lower.txt！")
    #写入新文件#
    Upper = open("Upper.txt","w")
    Upper.writelines(Upper_Letter.upper())
    Upper.close()
    print("已写入Upper.txt！")

#交叉写入#
def Cross_Write():
    #还是刚才那两个文件#
    #读取第一个文件#
    Lower = open("Lower.txt","r")
    Lower_Text = Lower.readlines()
    Lower.close()
    print("已读取Lower.txt！")
    #读取第二个文件#
    Upper = open("Upper.txt","r")
    Upper_Text = Upper.readlines()
    Upper.close()
    print("已读取Upper.txt！")
    #交错内容#
    Cross_Text = list(chain.from_iterable(zip(Lower_Text,Upper_Text)))
    #生成文件#
    Cross = open("Cross.txt","w")
    Cross.writelines(Cross_Text)
    Cross.close()
    print("已写入Cross.txt！")

#合并排序#
def Combine_File():
    #就读取刚刚第一个文件的头两行吧#
    #我不太想生成太多文件#
    #读取第一个文件的第一行#
    Lower = open("Lower.txt","r")
    Lower_Text1 = Lower.readline()
    Lower_Text1 = Lower_Text1[:-1]
    print("已读取Lower.txt的第一行！")
    #读取第一个文件的第二行#
    Lower_Text2 = Lower.readline()
    Lower_Text2 = Lower_Text2[:-1]
    print("已读取Lower.txt的第二行！")
    #混合并排序文件内容#
    Text = Lower_Text1 + Lower_Text2
    Text = list(Text)
    Text = sorted(Text, key=str.lower)
    print("已混合并排序文件内容！")
    #生成并写入文件Combine.txt#
    Combine = open("Combine.txt","w")
    Combine.writelines(Text)
    Combine.close()
    print("已将结果写入Combine.txt！")

Lower_to_Upper()
Cross_Write()
Combine_File()