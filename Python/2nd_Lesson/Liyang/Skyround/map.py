#!/usr/bin/python
# -*- coding:UTF-8 -*-

import numpy
import random
random.seed()

def cat_map_data(width, length, difficulty):
    "创建游戏的地形数据"

    '''
    地形参数列表
    0, 普通地形, 可刷怪, 无任何特殊效果, 消耗方块消耗后的基底方块
    1, 石块, 石块有较大的生命值和护甲, 难以摧毁, 但不会攻击, 消耗性方块
    2, 酒馆, 可选择恢复生命或恢复魔法值, 非消耗性方块
    3, boss, 不同于小怪, boss位置固定,血厚攻高, 较难打败, 消耗性方块
    99,出口
    -1,主角出生地
    '''
    #难度参数设置 difficulty = 1 or 2 or 3 or 4 or 5
    rock_density = 0.1 * difficulty
    tavern_density = 0.001 * (5 - difficulty)
    boss_density = 0.005 * difficulty

    #game_ground = [([0]*length) for creat_width in range(width)] 
    #初始化地形
    #使用numpy生成初始地形
    game_ground = numpy.random.random((width+1, length+1))
    
    for map_width in range(width):
        for map_length in range(length):
            if game_ground[map_width, map_length]<rock_density:
                game_ground[map_width, map_length] = 1
            elif game_ground[map_width, map_length]<rock_density+tavern_density:
                game_ground[map_width, map_length] = 2
            elif game_ground[map_width, map_length]<rock_density+tavern_density+boss_density:
                game_ground[map_width, map_length] = 3
            else:
                game_ground[map_width, map_length] = 0
    
    #设置出口和主角出生地
    exit_width = random.randint(0,width-1)
    exit_length = random.randint(0,length-1)
    role_width = random.randint(0,width-1)
    role_length = random.randint(0,length-1)

    game_ground[exit_width, exit_length] = 99
    game_ground[role_width, role_length] = -1
    
    return game_ground