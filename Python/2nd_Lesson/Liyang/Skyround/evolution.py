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

def update_map_data(hero_property, map_data, key_press):
    hero_pos = find_hero(map_data)
    next_step = cat_next_block(map_data, key_press)
    
    move_define = jud_go(map_data, key_press)
    
    if move_define == 0:
        map_data[hero_pos[0]][hero_pos[1]] = 0
        map_data[next_step[0]][next_step[1]] = -1 #走过的位置变为普通方块，下一位置变为英雄所在位置
    elif move_define == 1 and hero_property['rock_destory']:
        map_data[hero_pos[0]][hero_pos[1]] = 0
        map_data[next_step[0]][next_step[1]] = -1
    return map_data

def block_activity(root, hero_property, map_data, key_press, difficulty):
    '在普通方块上, 随机生成怪物'
    next_step = cat_next_block(map_data, key_press)
    next_element = map_data[next_step[0]][next_step[1]]
    re_property = hero_property
    
    jud_continue = 0

    if next_element == 1:
        if askyesno("讨厌的石头",'是否要打破石头'):
            hero_property['rock_destory'] = True
            re_property = battle_creat(root, hero_property, difficulty, 1)
    elif next_element == 2:
        re_property = heal_hero(hero_property, difficulty)
    elif next_element == 3:
        re_property = battle_creat(root, hero_property, difficulty,3)
    elif next_element == 98:
        re_property = find_key(hero_property)
    elif next_element == 99:     
        if hero_property['key'] == 'FOUND!':
            if level_clear(hero_property):
                jud_continue = 1
            else:
                jud_continue = -1
        else:
            showinfo(title = '门锁', message = '您还没有钥匙, 钥匙会随机出现在营地(橙色方块)当中')
    else:
        if random.random() < 0.15 * difficulty:
            re_property = battle_creat(root, hero_property, difficulty, 0)
    return jud_continue, re_property

def level_clear(hero_property):
    if hero_property['esp'] > 10:
        showinfo(title = '成就', message = hero_property['name']+'一局中逃跑超过十次, 获得“以无招胜有招”的称号...')
    if hero_property['esp'] == 0:
        showinfo(title = '成就', message = hero_property['name']+'一局中从未逃跑一局, 获得“不怂,就是干!”的称号...')
    choice_continue = askyesno("Skyround",'是否继续探索下一区域')
    return choice_continue