#!/usr/bin/python 
# -*- coding:UTF-8 -*-

import random
from Tkinter import * 
from role import get_enemy
from tkMessageBox import *
import time



def battle_creat(root, hero_property, difficulty, enemy_kind):
    '创建怪物信息'
    #1-->10:石头
    #2-->酒馆
    #3-->7,8,9 :boss
    #0-->0,1,2,3,4,5,6: 小怪
    
    dif_level = int(difficulty * (hero_property['level']+1))
    esp_before = hero_property['esp']
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

    exp = 0
    for add_exp_cir in enemy_property:
        exp += add_exp_cir['exp']
    plot_battle_sys(root, hero_property, enemy_property, exp)
    
    return hero_property


def level_sys(hero_property):
    global exp
    if hero_property['level'] < 51:
        hero_property['exp'] += exp
        showinfo(title = '胜利！', message = '获得'+str(exp)+'点经验')
        hero_level = int(hero_property['exp']**0.5)

        if hero_property['level'] != hero_level:
            hero_property['maxHP'] += 3 * hero_property['Armor']
            hero_property['maxMP'] +=   hero_property['Attack'] / 10
            hero_property['Attack'] += hero_property['maxMP'] / 10
            hero_property['Armor'] += 10 - hero_property['Armor']/10
            hero_property['level'] = hero_level
            hero_property['HP'] = hero_property['maxHP']
            hero_property['MP'] = hero_property['maxMP']

    return hero_property
        
def find_key(hero_property):
    showinfo(title = '找到钥匙', message = '恭喜你, 找到了出口钥匙!')
    hero_property = hero_property
    hero_property['key'] = 'FOUND!'
    return hero_property

def heal_hero(hero_property, difficulty):  
    showinfo(title = '运气不好', message = '没有找到钥匙, 但HP和MP得到恢复')
    hero_property = hero_property
    hero_property['HP'] = hero_property['maxHP']
    hero_property['MP'] = hero_property['maxMP']
    return hero_property

#####################################################core调用
def enemy_attack_you(hero_property, enemy_property):
    for num in range(len(enemy_property)):
        single_enemy_attack_value = enemy_property[num]['Attack'] * (100-hero_property['Armor']) / random.randint(90,110)
        if hero_property['MP']<0:
            single_enemy_attack_value *= 2
        hero_property['HP'] -= single_enemy_attack_value
        battleinfo_list.insert (0, enemy_property[num]['name']+'使用普通攻击对'+ \
                            hero_property['name']+'造成了'+str(single_enemy_attack_value)+'点伤害')
    return

def attack_enemy(enemy_num):
    global hero_property
    hero_attack_value = hero_property['Attack'] * (100-enemy_property[enemy_num]['Armor']) / random.randint(90,110)
    enemy_property[enemy_num]['HP'] -= hero_attack_value
    battleinfo_list.insert (0, hero_property['name']+'使用普通攻击对'+ \
                            enemy_property[enemy_num]['name']+'造成了'+str(hero_attack_value)+'点伤害')

    if enemy_property[enemy_num]['HP'] <= 0:
        del enemy_property[enemy_num]
    if enemy_property == []:
        hero_property = level_sys(hero_property)
        battle_window.withdraw()
    enemy_attack_you(hero_property,enemy_property)
    if hero_property['HP']<=0:
        hero_property['die'] = True
        showinfo(title = '失败', message = hero_property['diemessage'])
        battle_window.quit()

    battle_canvas.delete(ALL)
    plot_battle_core()
    return


def use_magic(enemy_num):
    global hero_property
    name = hero_property['hero_class']
    if hero_property['MP']>=hero_property['costMP']:
        if name == 'WARRIOR':
            hero_property['MP'] -= hero_property['costMP']
            hero_attack_value = hero_property['Attack'] * (100-enemy_property[enemy_num]['Armor']) / random.randint(90,110) * 5
            enemy_property[enemy_num]['HP'] -= hero_attack_value
            battleinfo_list.insert (0, hero_property['name']+'使用'+hero_property['Magicskill']+'对'+ \
                                    enemy_property[enemy_num]['name']+'造成了'+str(hero_attack_value)+'点伤害')
        elif name == 'MAGES':
            hero_attack_value = hero_property['Attack'] * random.randint(1,3)
            hero_property['MP'] -= hero_property['costMP']
            enemy_property[enemy_num]['HP'] -= hero_attack_value
            battleinfo_list.insert (0, hero_property['name']+'使用'+hero_property['Magicskill']+'对'+ \
                                    enemy_property[enemy_num]['name']+'造成了'+str(hero_attack_value)+'点伤害')  
        elif name == 'KNIGHT':
            hero_attack_value = hero_property['Attack'] * (100-enemy_property[enemy_num]['Armor']) / random.randint(90,110) / 2
            hero_property['MP'] -= hero_property['costMP']
            for sing_enemy in enemy_property:
                sing_enemy['HP'] -= hero_attack_value
            battleinfo_list.insert (0, hero_property['name']+'使用'+hero_property['Magicskill']+'对全体敌人'\
                                        +'造成了'+str(hero_attack_value)+'点伤害')
        elif name == 'PRIESTS':
            hero_attack_value = hero_property['Attack'] * (100-enemy_property[enemy_num]['Armor']) / random.randint(90,110) / 2
            hero_property['MP'] -= hero_property['costMP']
            enemy_property[enemy_num]['HP'] -= hero_attack_value
            hero_property['HP'] += hero_attack_value
            battleinfo_list.insert (0, hero_property['name']+'使用'+hero_property['Magicskill']+'向'+ \
                                    enemy_property[enemy_num]['name']+'吸取了'+str(hero_attack_value)+'点生命值')
    else:
        hero_property['MP'] -= hero_property['costMP']
        battleinfo_list.insert (0, hero_property['name']+'没有注意自己的魔法值不够, 耗尽了全部力气也未能放出技能,\
                          MP变为负数...更糟糕的是, 由于负的MP值导致他在怪物面前暴露了自己的弱点, 之后受到伤害*2')

    if enemy_property[enemy_num]['HP'] <= 0:
        del enemy_property[enemy_num]
    if enemy_property == []:
        hero_property = level_sys(hero_property)
        battle_window.withdraw()
    enemy_attack_you(hero_property,enemy_property)
    if hero_property['HP']<=0:
        hero_property['die'] = True
        showinfo(title = '失败', message = hero_property['diemessage'])
        battle_window.quit()

    battle_canvas.delete(ALL)
    plot_battle_core()
    return 

def escape():
    global hero_property
    hero_property['esp'] += 1
    showinfo(title = '逃跑', message = hero_property['name']+'坚信留得青山在, 不怕没柴烧的真理, 机智地逃脱了.')
    battle_window.withdraw()
    return

#####################################################


def plot_battle_core():
    global enemy_property, hero_property, hero_img_file
    enemy_oval = []
    
    battle_canvas.create_rectangle(1000,20,1260,620, fill = 'brown', outline = 'gray', width = 2)
    hero_img_file = PhotoImage(file = "image/boss.gif")
    battle_canvas.create_image(1130, 140, image = hero_img_file)

    battle_canvas.create_rectangle(1060,590 - 300 * hero_property['HP']/hero_property['maxHP'],1100,590, fill = 'red' )
    battle_canvas.create_rectangle(1160, 590 - 300 * hero_property['MP']/hero_property['maxMP'],1200,590, fill = 'blue')

    battle_canvas.create_text(1080,270, text = 'HP', fill = 'white', font = "time 25 bold") 
    battle_canvas.create_text(1180,270, text = 'MP', fill = 'white', font = "time 25 bold") 
    battle_canvas.create_text(1080,600, text = hero_property['HP'], fill = 'white', font = "time 15") 
    battle_canvas.create_text(1180,600, text = hero_property['MP'], fill = 'white', font = "time 15") 

    for plot_enemy_cir in range(len(enemy_property)):
            center_oval = random.randint(300,600)
            radii_oval = enemy_property[plot_enemy_cir]['HP']/10
            enemy_oval.append(battle_canvas.create_oval(center_oval-radii_oval,center_oval-radii_oval, \
                                          center_oval+radii_oval,center_oval+radii_oval, fill = 'black'))
            battle_canvas.create_text(center_oval,center_oval, \
                                      text = enemy_property[plot_enemy_cir]['name'], \
                                      fill = 'white', font = "time 10 bold")
      
    battle_label = Label(battle_frame, text = '本局动作', font = 'time 20 bold')
    battle_label.grid(row = 1, column = 1, columnspan = 3)

    button_attack = Menubutton(battle_frame, text='普通攻击', width=15, font = 'time 15 bold', height=1)
    attack_enemy_select = Menu(button_attack,tearoff=False)
    for num_attack in range(len(enemy_property)):
        attack_enemy_select.add_radiobutton(label=enemy_property[num_attack]['name'], \
                   command=lambda num_attack=num_attack:attack_enemy(num_attack))
    button_attack.config(menu=attack_enemy_select)

    button_magic = (Menubutton(battle_frame, text='特殊技能:'+hero_property['Magicskill'] \
                                            , width=15, font = 'time 15 bold', height=1))
    magic_enemy_select = Menu(button_magic)
    for num_magic in range(len(enemy_property)):
        magic_enemy_select.add_radiobutton(label=enemy_property[num_magic]['name'], \
                   command=lambda num_magic=num_magic:use_magic(num_magic))
    button_magic.config(menu=magic_enemy_select)

    button_escape = Button(battle_frame, text="仓皇逃跑", width=15, font = 'time 15 bold', height=1, command = escape)
    
    button_attack.grid(row = 2, column = 1)
    button_magic.grid(row = 2, column = 2)
    button_escape.grid(row = 2, column = 3)
    blank_label.grid(row = 1, column = 4, rowspan = 2)
    battleinfo_list.grid(row = 1, column = 5, rowspan = 2)
    return

def plot_battle_sys(root, in_hero_property, in_enemy_property,in_exp):
    global battle_canvas, battle_window, battle_frame, battleinfo_list, blank_label
    global enemy_property, hero_property, exp
    global hero_img_file
    hero_property = in_hero_property
    enemy_property = in_enemy_property
    center_oval_jud = 0
    creat_center_oval = []
    exp = in_exp

    
    battle_window = Toplevel(root)
    battle_window.protocol('WM_DELETE_WINDOW', lambda:showinfo(title='警告', message='即将失去同步'))
    battle_window.title('BATTLE')
    battle_window.geometry("1280x720+80+40") 

    battle_canvas = Canvas(battle_window,  width = 1280, height = 640, bg = 'orange')
    battle_canvas.pack()
    
    battle_frame = Frame(battle_window)
    battle_frame.pack()
    
    blank_label = Label(battle_frame, text = ' '*35)
    battleinfo_list = Listbox(battle_frame, font = 'time 15 bold', bg = 'black', \
                                  fg = 'white', width=60, height=3, yscrollcommand = Scrollbar().set)

    plot_battle_core()

    return hero_property, enemy_property
