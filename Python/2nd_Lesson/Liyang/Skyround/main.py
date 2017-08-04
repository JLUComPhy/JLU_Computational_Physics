#!/usr/bin/python
# -*- coding:UTF-8 -*-

from evolution import *
from map import *
from role import *
from Tkinter import *
from gplot import *

WIDTH = 72
LECNGTH = 118
first_cir = False

print ("==============================================")
print ("==================Skyround====================")
print ("==============================================")
print ("欢迎来到skyround的世界!")
print ("请输入主角的名字")
hero_name = raw_input('>')
print ("请确认游戏的难度(输入1～5的整数)")
diff_chioce = int(raw_input('>'))
print ("请选择你的职业")
print ("---输入代号---")
print ("1,战士")
print ("2,法师")
print ("3,骑士")
print ("4,牧师")
print ("------------")
hero_kind = int(raw_input(">"))
print ("=============选择结束, 正在初始化游戏==============")

map_data = cat_map_data(WIDTH, LECNGTH, diff_chioce)
hero_property = get_hero(hero_name, hero_kind)
#game_plot(root, map_data, WIDTH, LECNGTH)

print ("============初始化完成!游戏窗口已生成!==============")

round_number = 1
root = Tk()
root.title('Skyround-Game'+ 'round%d' %round_number)
canvas = Canvas(root, bg="white")
#=======================================
#按键的读取
def call_back(event):
    'callback'
    global map_data, root, canvas, WIDTH, LECNGTH, round_number, diff_chioce, first_cir
   
    key_press = event.keysym


    if key_press == '0' or first_cir: #第一次按键，按下0开始游戏
        first_cir = True
        hero_pos = 0
        next_pos = 0
       
        if key_press != '0':
            hero_pos = find_hero(map_data)
            next_pos = cat_next_block(map_data, key_press)

        quit_judage = block_activity(root, map_data, key_press, diff_chioce)
        map_data = update_map_data(map_data, key_press)
        game_plot(canvas, map_data, WIDTH, LECNGTH, hero_pos, next_pos)   
        if quit_judage == 1:
            hero_pos = 0
            next_pos = 0
            round_number += 1
            map_data = cat_map_data(WIDTH, LECNGTH, diff_chioce)
            root.title('Skyround-Game'+ '  round%d' %round_number)
            game_plot(canvas, map_data, WIDTH, LECNGTH, hero_pos, next_pos)   
        elif quit_judage == -1:
            root.quit()
        else:
            pass
    return
#接受按键
root.bind("<Key>", call_back)
#更新地图
#仅选中时有效
root.focus_set()
#进入下一个循环
root.mainloop()
#按键读取完毕
#========================================


print ("============GAME CLOSED!==============")