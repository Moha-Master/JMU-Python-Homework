#运行代码以获得最佳效果#
import jieba as Jb
import tkinter as Tk
import wordcloud as Wc
from random import randint

#生成GUI界面#
root = Tk.Tk()
root.geometry("1920x1080")
root.mainloop

def pic_generate():
    file = open("D:\\text.txt", encoding = "utf-8")#读取文件#
    text = file.read()
    file.close()
    text_list = Jb.lcut(text)#处理文字#
    length = len(text_list)
    number = 0
    for i in range(length): # 筛选一个字的分词并去掉它
        if len(text_list[i-number]) == 1:
            del text_list[i-number]
            number += 1
        else:
            continue
    text_list = " ".join(text_list) # 添加空格分隔符
    def random_color_func(word=None, 
                          font_size=None,
                          position=None, 
                          orientation=None,
                          font_path=None,
                          random_state=None):
            h  = randint(0,360)
            s = int(100.0 * 255.0 / 255.0)
            l = int(100.0 * float(randint(60, 120)) / 255.0)
            return "hsl({}, {}%, {}%)".format(h, s, l)#色彩控制#
    Pic = Wc.WordCloud(width = 1920,
                       height = 1080,
                       min_font_size = 12,
                       font_path = "C:\\Windows\\Fonts\\Noto Sans CJK SC\\NotoSansCJKsc-Bold.otf",
                       background_color = "#FFFFFF",
                       color_func = random_color_func,
                       relative_scaling = 1)#图片选项#
    Pic.generate(text_list)#生成图片#