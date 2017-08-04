#!/usr/bin/python
# -*- coding:UTF-8 -*-

import random
from Tkinter import *
from battle import *
from tkMessageBox import *



def move_char_judage(key_press):
    '定义 输入 --- 移动 的对应关系'
    if key_press == 'w' or key_press == 'W':
        move_step = [-1, 0]
    elif key_press == 's' or key_press == 'S':
        move_step = [1, 0]
    elif key_press == 'a' or key_press == 'A':
        move_step = [0, -1]
    elif key_press == 'd' or key_press == 'D': 
        move_step = [0, 1]
    else:
        move_step = [0, 0]
    return move_step

def find_hero(map_data):
    '确定英雄的位置'
    hero_pos = [0,0]
    for search_width in range(len(map_data)):
        for search_length in range(len(map_data[0])):
            if map_data[search_width][search_length] == -1:
                hero_pos[0] = search_width
                hero_pos[1] = search_length
    return hero_pos

def cat_next_block(map_data, key_press):
    '获取下一个方格的坐标'
    hero_pos = find_hero(map_data)
    hero_move = move_char_judage(key_press)
    next_step = hero_pos
    next_step = [hero_pos[0]+hero_move[0], hero_pos[1]+hero_move[1]]
    return next_step

def jud_go(map_data, key_press):
    '判断下一个方格是否能走'
    hero_pos = find_hero(map_data)
    next_step = cat_next_block(map_data, key_press)
    if map_data[next_step[0]][next_step[1]] == 1: #如果前方是石块
        move_def = 1
    elif map_data[next_step[0]][next_step[1]] == 99:
        move_def = 99
    elif next_step[0]>len(map_data)-2 \
          or (next_step[1]>len(map_data[0])-2 \
          or next_step[0]<0 \
          or next_step[1]<0): #如果已到达边界
        move_def = -1
    else:
        move_def = 0
    return move_def

def update_map_data(map_data, key_press):
    hero_pos = find_hero(map_data)
    next_step = cat_next_block(map_data, key_press)
    
    move_define = jud_go(map_data, key_press)
    
    if move_define == 0:
        map_data[hero_pos[0]][hero_pos[1]] = 0
        map_data[next_step[0]][next_step[1]] = -1 #走过的位置变为普通方块，下一位置变为英雄所在位置
    elif move_define == 99:
        map_data[hero_pos[0]][hero_pos[1]] = 0
    return map_data

def block_activity(root, map_data, key_press, difficulty):
    '在普通方块上, 随机生成怪物'
    next_step = cat_next_block(map_data, key_press)
    next_element = map_data[next_step[0]][next_step[1]]
    
    jud_continue = 0
    if next_element == 1:
        rock_battle_creat(root, difficulty)
    elif next_element == 2:
        tavern_heal_creat(root, difficulty)
    elif next_element == 3:
        boss_battle_creat(root, difficulty)
    elif next_element == 99:    
        if level_clear():
            jud_continue = 1
        else:
            jud_continue = -1
    else:
        if random.random < 0.15*difficulty:
            enemy_battle_creat(root, difficulty)
    return jud_continue

def level_clear():
    choice_continue = askyesno("Skyround",'胜利！是否继续下一区域')
    return choice_continue
