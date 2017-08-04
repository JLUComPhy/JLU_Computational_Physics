#!/usr/bin/python 
# -*- coding:UTF-8 -*-

import random
random.seed()

def get_hero(hero_name, hero_class):
    "职业选择和人物属性设置"
   
    '''
    英雄职业选择：
    1，战士，血厚攻低，眩晕技能
    2，法师，血薄攻高，燃烧技能
    3，骑士，平均分配，爆击技能
    4，牧师，随机性大，加血技能
    '''
    
    hero_property = {'hero_class':'warrior', 'name':hero_name, 'HP':100, 'MP':30, 'Attack':10, 'Armor':0}

    if hero_class == 1:
        hero_property['hero_class'] = 'warrior'
        hero_property['HP'] = random.randint(100,150)
        hero_property['MP'] = random.randint(0,10)
        hero_property['Attack'] = random.randint(5,10)
        hero_property['Armor'] = random.randint(20,40)
    elif hero_class == 2:
        hero_property['hero_class'] = 'mages'
        hero_property['HP'] = random.randint(20,60)
        hero_property['MP'] = random.randint(100,300)
        hero_property['Attack'] = random.randint(20,30)
        hero_property['Armor'] = random.randint(0,10)
    elif hero_class == 3:
        hero_property['hero_class'] = 'knight'
        hero_property['HP'] = random.randint(80,100)
        hero_property['MP'] = random.randint(20,100)
        hero_property['Attack'] = random.randint(12,19)
        hero_property['Armor'] = random.randint(10,20)
    elif hero_class == 4:
        hero_property['hero_class'] = 'priests'
        hero_property['HP'] = random.randint(10,200)
        hero_property['MP'] = random.randint(10,100)
        hero_property['Attack'] = random.randint(5,30)
        hero_property['Armor'] = random.randint(0,50)
    
    return hero_property


def get_enemy(enemy_kind):
    '选取敌对生物函数'
    """
    敌对生物种类
    0, flower: 只是一个装饰
    1，snake:基本的低级小怪
    2，wolf:有一定攻击力的小怪
    3，eagle:较为灵活的小怪
    4，zombie:血厚攻低的中等怪物
    5，robber: 血薄攻高的中等怪物
    6，drunkenrobber: 攻击血量十分随缘的怪物
    7，robberleader:Boss1, 血中等，攻极其高
    8，treant, 血极其厚，攻击力中等
    9，kid, 十分随缘的boss(有几率一击必杀主角)
    """

    
    if enemy_kind == 1:
        enemy_data = {'name':'snake', 'HP':random.randint(20,30), 'MP':random.randint(0,10), \
                               'Attack':random.randint(5,15), 'Armor':random.randint(0,10)}
    elif enemy_kind == 2:
        enemy_data = {'name':'wolf', 'HP':random.randint(40,60), 'MP':random.randint(0,50), \
                               'Attack':random.randint(10,30), 'Armor':random.randint(10,20)}
    elif enemy_kind == 3:
        enemy_data = {'name':'eagle', 'HP':random.randint(10,50), 'MP':random.randint(60,90), \
                               'Attack':random.randint(10,40), 'Armor':random.randint(30,40)}
    elif enemy_kind == 4:
        enemy_data = {'name':'zombie', 'HP':random.randint(100,150), 'MP':random.randint(10,70), \
                               'Attack':random.randint(10,40), 'Armor':random.randint(10,30)}
    elif enemy_kind == 5:
        enemy_data = {'name':'robber', 'HP':random.randint(60,100), 'MP':random.randint(20,60), \
                               'Attack':random.randint(20,40), 'Armor':random.randint(20,50)}
    elif enemy_kind == 6:
        enemy_data = {'name':'drunkenrobber', 'HP':random.randint(1,200), 'MP':random.randint(0,200), \
                               'Attack':random.randint(0,50), 'Armor':random.randint(0,60)}
    elif enemy_kind == 7:
        enemy_data = {'name':'robberleader', 'HP':random.randint(100,120), 'MP':random.randint(200,300), \
                               'Attack':random.randint(50,60), 'Armor':random.randint(50,60)}
    elif enemy_kind == 8:
        enemy_data = {'name':'treant', 'HP':random.randint(500,700), 'MP':random.randint(200,600), \
                               'Attack':random.randint(10,30), 'Armor':random.randint(50,80)}
    elif enemy_kind == 9:
        enemy_data = {'name':'kid', 'HP':random.randint(1,1000), 'MP':random.randint(0,600), \
                               'Attack':random.randint(0,300), 'Armor':random.randint(0,90)}
    else:
        enemy_data = {'name':'flower', 'HP':random.randint(1,5), 'MP':0, \
                               'Attack':0, 'Armor':0}


    return enemy_data