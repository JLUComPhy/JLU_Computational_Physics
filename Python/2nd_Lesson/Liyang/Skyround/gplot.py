#!/usr/bin/python
# -*- coding:UTF-8 -*-

from Tkinter import *
from evolution import find_hero

def game_plot(root, canvas, map_data, map_width, map_length, hero_pos, next_pos,hero_property):
    '初始化地图形状'
    

    if hero_pos and next_pos: #分情况绘制，节省内存
        update_plot(canvas, map_data, hero_pos, next_pos)
    else:   
        init_plot(canvas, map_data, map_width, map_length)
    
    plot_hero_hub(canvas, map_width, map_length, hero_property)
    return


def init_plot(canvas, map_data, map_width, map_length):
    '绘制方形网格窗口'
    '''
    blue : 主角自己
    white: 普通方块
    red: boss
    yellow: 酒馆
    black: 石块
    green: 出口
    '''
    screen_length = map_length * 10 + 20 + 300
    screen_width = map_width * 10 + 20
    canvas.config(width=screen_length,height=screen_width)
    
    for plot_width in range(map_width):
        for plot_length in range(map_length):
            #绘制方块
            plot_core(canvas, map_data[plot_width][plot_length], plot_width, plot_length)
    canvas.update()
    return

def plot_core(canvas, input_number, plot_width, plot_length):
    '绘图核心代码, 判断方块颜色, 并绘制'
    if input_number == 1:
        plot_color = 'brown'
    elif input_number == 2:
        plot_color = 'orange'
    elif input_number == 3:
        plot_color = 'red'
    elif input_number == 99:
        plot_color = 'green'
    elif input_number == 98:
        plot_color = 'orange'#'cyan'
    elif input_number == -1:
        plot_color = 'blue'
    else:
        plot_color = 'white'

    canvas.create_rectangle(10+10*plot_length, 10+10*plot_width, 
    10+10*(plot_length+1), 10+10*(plot_width+1) ,fill=plot_color,outline="black")                       
    return 

def update_plot(canvas, map_data, hero_pos, next_pos):
    plot_core(canvas, map_data[hero_pos[0]][hero_pos[1]], hero_pos[0], hero_pos[1])
    plot_core(canvas, map_data[next_pos[0]][next_pos[1]], next_pos[0], next_pos[1])
    canvas.update()
    #print 'simple'
    return

def plot_hero_hub(canvas, map_width, map_length, hero_property):
    '绘制英雄属性窗口'
    global hero_img_file #将英雄图片作为全局变量，否则无法输出

    frame_begin_pos = [10, map_length * 10 + 30]
    frame_end_pos = [map_width * 10 + 10, map_length * 10 + 280] 
    hero_image_pos = [frame_begin_pos[0] + 120, frame_begin_pos[1]+ 125]  #[width, length]
    text_heroclass_pos = [hero_image_pos[0] + 130, hero_image_pos[1]]
    text_heroname_pos = [text_heroclass_pos[0] + 21, text_heroclass_pos[1]]
    text_level_pos = [text_heroname_pos[0] + 30, text_heroname_pos[1]]
    text_HP_pos = [text_level_pos[0] + 60, text_level_pos[1]]
    text_MP_pos = [text_HP_pos[0] + 40, text_HP_pos[1]]
    text_attack_pos = [text_MP_pos[0] + 40, text_MP_pos[1]]
    text_armor_pos = [text_attack_pos[0] + 40, text_attack_pos[1]]
    text_key_pos = [text_armor_pos[0] + 100, text_armor_pos[1]]
    
    #HUB窗体
    canvas.create_rectangle(frame_begin_pos[1], frame_begin_pos[0], frame_end_pos[1], frame_end_pos[0] \
                           ,fill = 'gray',outline="black", width = '1')

    #人物图片
    hero_img_file = PhotoImage(file = "image/hero.gif")
    canvas.create_image(hero_image_pos[1], hero_image_pos[0], image = hero_img_file)


    canvas.create_text(text_heroclass_pos[1], text_heroclass_pos[0], text = hero_property['hero_class'] \
                      ,fill = 'black', font = "time 30 bold") 
    canvas.create_text(text_heroname_pos[1], text_heroname_pos[0], text = hero_property['name'] \
                      ,fill = 'black', font = "time 15 underline") 
    canvas.create_text(text_level_pos[1], text_level_pos[0], text = ['level', hero_property['level']] \
                      ,fill = 'blue', font = "time 20") 
    canvas.create_text(text_HP_pos[1], text_HP_pos[0], text = ['HP:', hero_property['HP'], '/', hero_property['maxHP']] \
                      ,fill = 'red', font = "time 25 bold") 
    canvas.create_text(text_MP_pos[1], text_MP_pos[0], text = ['MP:', hero_property['MP'], '/', hero_property['maxMP']] \
                      ,fill = 'blue', font = "time 25 bold") 
    canvas.create_text(text_attack_pos[1], text_attack_pos[0], text = ['ATTACK:', hero_property['Attack']] \
                      ,fill = 'red', font = "time 25 bold") 
    canvas.create_text(text_armor_pos[1], text_armor_pos[0], text = ['ARMOR:', hero_property['Armor']] \
                      ,fill = 'blue', font = "time 25 bold") 
    canvas.create_text(text_key_pos[1], text_key_pos[0], text = ['KEY:', hero_property['key']] \
                      ,fill = 'red', font = "time 30 bold") 
    return