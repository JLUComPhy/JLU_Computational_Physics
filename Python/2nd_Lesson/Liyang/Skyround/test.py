#!/usr/bin/python
# -*- coding:UTF-8 -*-

from Tkinter import * 

root = Tk()
root.title('Skyround-Game')
#=======================================
#按键的读取
key_press = 'w'
def call_back(event):
    'callback'
    global key_press
    key_press = event.keysym
    print key_press == '0' or 
    return

#接受按键
root.bind("<Key>", call_back)
root.focus_set()
#进入下一个循环
root.mainloop()
#按键读取完毕
#========================================