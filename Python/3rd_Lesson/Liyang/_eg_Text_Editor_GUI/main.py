#! /usr/bin/python 
# -*- coding:UTF-8 -*-
#Python支持多种图形界面的库，为了不再麻烦去下载新的库，这里直接使用了python自带的tkinter库，记住本代码主要为了练习实现一个简单的GUI界面，顺便熟悉一下tkinter的使用
from Tkinter import *  
import os
#from Tkinter import filedialog

def die():
    root.destroy()
     
class Create: 
    # init函数定义类的一些属性
    def __init__(self,root):
        self.root=(root) 
        #菜单控件；显示菜单栏,下拉菜单和弹出菜单，明显这里是要创建基于root的顶层菜单，记住名字self.menubar
        self.menubar=Menu(root)   
        #Text是tkinter中的文本控件，用于显示多行文本
        self.textpad = Text(root)
        self.textpad.pack(expand=YES,fill=BOTH)#expand 允许拉伸，fill允许（xy两个方向）填充
    
       #这里，是要创建基于顶层菜单的下拉菜单，记住它的名字self.filemenu
        self.filemenu=Menu(self.menubar,tearoff=0)  
        #好吧，开始添加命令吧，记得要把实现方法添加到command属性中，顺便提一下menu的属性：label,command,accelerator,underline
        self.filemenu.add_command(label="新建",accelerator="Ctrl+N")  
        self.filemenu.add_command(label="打开",command=self.openfile)  
        self.filemenu.add_separator()  
        self.filemenu.add_command(label="保存",command=self.save)
        self.filemenu.add_command(label="另存为",command=self.donothing)  
        self.filemenu.add_separator()  
        self.filemenu.add_command(label="页面设置",accelerator="U",command=self.donothing)  
        self.filemenu.add_command(label="打印",accelerator="Ctrl+P",command=self.donothing)  
        self.filemenu.add_separator()  
        self.filemenu.add_command(label="退出",accelerator="X",command=die)
        #好了，创建完毕就级联到顶层菜单上吧，顺便给它们起一个名字“文件”  
        self.menubar.add_cascade(label="文件",menu=self.filemenu)  
        
        self.editmenu = Menu(self.menubar, tearoff=0)  
        self.editmenu.add_command(label="Undo", command=self.donothing)  
        self.editmenu.add_command(label="Cut", command=self.donothing)  
        self.editmenu.add_command(label="Copy", command=self.donothing)  
        self.menubar.add_cascade(label="edit",menu=self.editmenu)

        self.helpmenu = Menu(self.menubar, tearoff=0)  
        self.helpmenu.add_command(label="Help Index", command=self.donothing)  
        self.helpmenu.add_command(label="About...", command=self.donothing)  
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)  
        
        self.root.config(menu=self.menubar)  
          
    def donothing(self):  
        filewin=Toplevel(self.root)  
        button=Button(filewin,text="hi，添加你的代码")  
        button.pack() 

    def openfile(self):
        #这里，也是在网上搜了一下发现有如此好用的函数，看来要用python实现一个东西时，一定要先去了解一下有没有好用的库
        filename = filedialog.askopenfilename(title = "打开",filetypes = [("文件","*.txt")])
        if filename == '':
            filename = None
        else:
            root.title('FileName:'+os.path.basename(filename))
            self.textpad.delete(1.0,END)
            f = open(filename,'r+')
            self.textpad.insert(1.0,f.read())
            f.close()
    
    def save(self):
        sname = filedialog.asksaveasfilename(title = "保存",filetypes = [("保存文件","*.txt")])
        f = open(sname,'w+')
        msg = self.textpad.get(1.0,END)
        f.write(msg)
        f.close()

if __name__ == "__main__":  

    root = Tk() #定义一个主窗口
    root.title('记事本') #看到title了吗？添加一个属性，名字叫记事本
    root.geometry("800x500") #几何布局，初始化主窗口的大小
    window = Create(root) #从这里开始正式调用Create实现一个记事本
    root.mainloop()
