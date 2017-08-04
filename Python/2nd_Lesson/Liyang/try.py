# 创建一个矩形，指定画布的颜色为白色

from Tkinter import *
root = Tk()
def callBack(event):
    key_press = event.keysym
    return
# 为明显起见，将背景色设置为白色，用以区别root
root.bind("<KeyPress-plus>", callBack)
#控件打包
root.pack()
#仅选中时有效
root.focus_set()
#更新地图
#进入下一个循环
root.mainloop()

global key_press

