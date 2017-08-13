#!/usr/bin/python
# -*- coding:UTF-8 -*-

from evolution import *
from map import *
from role import *
from Tkinter import *
from gplot import *

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
########################初始化参数模块#################################
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

WIDTH = 72
LECNGTH = 118
first_cir = False
round_number = 1 #记录游戏轮数


print ("==============================================")
print ("==================Skyround====================")
print ("==============================================")
print ("欢迎来到skyround的世界!")
print ("请输入主角的名字")
hero_name = raw_input('>>> ')
if hero_name == '':
    hero_name = 'NOOB'
print ("请确认游戏的难度(输入1～5的整数)")
diff_chioce = raw_input('>>> ')
if diff_chioce == '':
    diff_chioce = 1
else:
    diff_chioce = int(diff_chioce)
print ("请选择你的职业")
print ("---输入代号---")
print ("1,战士")
print ("2,法师")
print ("3,骑士")
print ("4,牧师")
print ("------------")
hero_kind = raw_input(">>> ")
if hero_kind == '':
    hero_kind = 1
else:
    hero_kind = int(hero_kind)
print ("=============选择结束, 正在初始化游戏==============")

map_data = cat_map_data(WIDTH, LECNGTH, diff_chioce)
hero_property = get_hero(hero_name, hero_kind)

print ("============初始化完成!游戏窗口已生成!==============")


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
########################callback模块#################################
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def move_plot(event):
    'callback'
    global map_data, root, canvas, WIDTH, LECNGTH, round_number
    global diff_chioce, first_cir, hero_property
   
    key_press = event.keysym

    if key_press == '0' or first_cir: #第一次按键，按下0开始游戏

        first_cir = True
        hero_pos = 0
        next_pos = 0
        quit_judage = 0
       
        if key_press != '0':
            hero_pos = find_hero(map_data)
            next_pos = cat_next_block(map_data, key_press)

            return_value =  block_activity(root, hero_property, map_data, key_press, diff_chioce)
            quit_judage = return_value[0]  #是否通关
            hero_property = return_value[1] #英雄属性变化
            
            map_data = update_map_data(hero_property, map_data, key_press)

        game_plot(root, canvas, map_data, WIDTH, LECNGTH, hero_pos, next_pos, hero_property) 

        if hero_property['die']:
            showinfo(title = 'GAME OVER', message = '游戏结束, 请重新来过...')
            root.quit()

        if quit_judage == 1:
            round_number += 1
            hero_property['key'] = 'Missing...'
            map_data = cat_map_data(WIDTH, LECNGTH, diff_chioce)
            root.title('Skyround: '+ 'floor-%d' %round_number)
            game_plot(root, canvas, map_data, WIDTH, LECNGTH, 0, 0, hero_property) 
        elif quit_judage == -1:
            root.quit()
        else:
            pass
    return

def begin_info(event): 
    global root
    if root.winfo_reqwidth() < 300:
        showinfo(title = '开始游戏', message = '按“0”开始游戏')
    return


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#####################======主程序=====################################
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
root = Tk() #定义主窗口

root.title('Skyround: '+ 'floor-%d' %round_number)
root.bind("<Button-2>", begin_info)
                   #开始提示对话框

canvas = Canvas(root, bg="white") #定义画板页
canvas.pack()

root.bind("<Key>", move_plot)
root.focus_set()
root.mainloop()    #绘图过程

print ("============GAME CLOSED!==============")