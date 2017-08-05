#!/usr/bin/python
# -*- coding:UTF-8 -*-
from Tkinter import * 

'''
tk = Tk()

load = Image.open('hero.jpg') 
render= ImageTk.PhotoImage(load)  

img = Label(tk, image=render)  
img.image = render
img.place(x= 0,y=0)

img.pack
'''
root = Tk()
canvas = Canvas(root, bg = "white")
canvas.pack()
hero_img_file = PhotoImage(file = "hero.gif")
canvas.create_image(0, 0, image = hero_img_file)
root.mainloop()
#========================================