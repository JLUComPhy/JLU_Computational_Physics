#!/usr/bin/python
# -*- coding:UTF-8 -*-

from Tkinter import *
from evolution import find_hero

def game_plot(canvas, map_data, map_width, map_length, hero_pos, next_pos):
    '初始化地图形状'
    canvas.pack()
    if hero_pos and next_pos: #分情况绘制，节省内存
        update_plot(canvas, map_data, hero_pos, next_pos)
    else:   
        init_plot(canvas, map_data, map_width, map_length)
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
    screen_length = map_length * 10 + 200 + 20
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
    if input_number == 0:
        plot_color = 'white'
    elif input_number == 1:
        plot_color = 'cyan'
    elif input_number == 2:
        plot_color = 'orange'
    elif input_number == 3:
        plot_color = 'red'
    elif input_number == 99:
        plot_color = 'green'
    elif input_number == -1:
        plot_color = 'blue'
    else:
        pass

    canvas.create_rectangle(10+10*plot_length, 10+10*plot_width, 10+10*(plot_length+1), 10+10*(plot_width+1) \
                                    ,fill=plot_color,outline="black")
    return 

def update_plot(canvas, map_data, hero_pos, next_pos):
    plot_core(canvas, map_data[hero_pos[0]][hero_pos[1]], hero_pos[0], hero_pos[1])
    plot_core(canvas, map_data[next_pos[0]][next_pos[1]], next_pos[0], next_pos[1])
    canvas.update()
    #print 'simple'
    return