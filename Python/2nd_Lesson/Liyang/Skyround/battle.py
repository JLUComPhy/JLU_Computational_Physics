#!/usr/bin/python 
# -*- coding:UTF-8 -*-

import random
from Tkinter import * 
from role import get_enemy
from tkMessageBox import *


def level_sys(hero_property, enemy_property):
    if hero_property['level'] < 51:
        exp = 0
        for add_exp_cir in range(len(enemy_property)):
            exp += enemy_property[add_exp_cir]['exp']
        hero_property['exp'] += exp
        hero_level = int(hero_property['exp']**0.5)

        if hero_property['level'] != hero_level:
        # showinfo(title = '升级提示', message = '恭喜您,升级啦！人物属性提升, 生命魔法全满')
            hero_property['maxHP'] += 3 * hero_property['Armor']
            hero_property['maxMP'] +=   hero_property['Attack'] / 10
            hero_property['Attack'] += hero_property['maxMP'] / 10
            hero_property['Armor'] += 10 - hero_property['Armor']/10
            hero_property['level'] = hero_level
            hero_property['HP'] = hero_property['maxHP']
            hero_property['MP'] = hero_property['maxMP']
    return hero_property

def battle_creat(hero_property, difficulty, enemy_kind):
    #1-->10:石头
    #2-->酒馆
    #3-->7,8,9 :boss
    #0-->0,1,2,3,4,5,6: 小怪
    
    dif_level = int(difficulty * (hero_property['level']+1))

    enemy_property = []
    if enemy_kind == 1: #rock
        enemy_property.append(get_enemy(10))
    if enemy_kind == 3: #boss
        enemy_property.append(get_enemy(random.choice([7,8,8,9,9,9])))
    if enemy_kind == 0: #小怪
        number_enemy = random.randint(1,difficulty+1)
        for cir_choose_enemy in range(number_enemy):
            enemy_list = []
            enemy_list.extend([0]*(int(dif_level +2)))
            enemy_list.extend([1]*(10-dif_level))
            enemy_list.extend([2]*(9-dif_level))
            enemy_list.extend([3]*(8-dif_level))
            enemy_list.extend([4]*(int(dif_level*0.6)))
            enemy_list.extend([5]*(int(dif_level*0.7)))
            enemy_list.extend([6]*(int(dif_level*0.8)))
            #print enemy_list
            enemy_property.append(get_enemy(random.choice(enemy_list)))

    win_or_not = plot_battle_sys(hero_property, enemy_property)
    if win_or_not:
        hero_property = level_sys(hero_property, enemy_property)
    else:
        hero_property['die'] = True
    return hero_property

def find_key(hero_property):
    showinfo(title = '找到钥匙', message = '恭喜你找到了出口钥匙!')
    hero_property = hero_property
    hero_property['key'] = 'FOUND!'
    return hero_property

def heal_hero(hero_property, difficulty):  
    showinfo(title = '运气不好', message = '没有找到钥匙, 但HP和MP得到恢复')
    hero_property = hero_property
    hero_property['HP'] = hero_property['maxHP']
    hero_property['MP'] = hero_property['maxMP']
    return hero_property

def plot_battle_sys(hero_property, enemy_property):
    '''
    battle_window = Tk()
    battle_window.title('BATTLE')
    
    battle_canvas = Canvas(battle_window, bg = 'brown')
    battle_canvas.pack()

    battle_canvas.create_rectangle(0, 300, 1000, 700, fill = 'gray')
    battle_window.mainloop()
    '''
    return True


