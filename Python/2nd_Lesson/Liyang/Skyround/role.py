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
    
    hero_property = {'hero_class':'WARRIOR', 'name':hero_name, 'HP':100, 'MP':30, 'Attack':10, \
                          'Armor':0 , 'maxHP':100, 'maxMP':30, 'key': 'Missing...', 'exp':0, 'level':0, \
                           'Magicskill':'致命一击' , 'costMP':'2','die': False, 'rock_destory':False, 'esp':0, \
                           'diemessage':'苟利国家生死以，岂因祸福避趋之!'}

    if hero_class == 1:
        hero_property['hero_class'] = 'WARRIOR'
        hero_property['HP'] = random.randint(1500,2000)
        hero_property['MP'] = random.randint(1,10)
        hero_property['Attack'] = random.randint(20,30)
        hero_property['Armor'] = random.randint(20,40)
        hero_property['costMP'] = 2
        hero_property['Magicskill'] = '致命一击'
        hero_property['diemessage'] = '苟利国家生死以，岂因祸福避趋之!'
    elif hero_class == 2:
        hero_property['hero_class'] = 'MAGES'
        hero_property['HP'] = random.randint(200,600)
        hero_property['MP'] = random.randint(100,300)
        hero_property['Attack'] = random.randint(100,120)
        hero_property['Armor'] = random.randint(0,10)
        hero_property['costMP'] = 25
        hero_property['Magicskill'] = '火球术'
        hero_property['diemessage'] = '我...我乃...冬堡大法师, 尔等鼠辈...速速退下! (口吐鲜血)咳,咳,咳...'
    elif hero_class == 3:
        hero_property['hero_class'] = 'KNIGHT'
        hero_property['HP'] = random.randint(800,1000)
        hero_property['MP'] = random.randint(20,100)
        hero_property['Attack'] = random.randint(80,100)
        hero_property['Armor'] = random.randint(10,20)
        hero_property['costMP'] = 10
        hero_property['Magicskill'] = '群体攻击'
        hero_property['diemessage'] = 'FOR THE KING!!!'
    elif hero_class == 4:
        hero_property['hero_class'] = 'PRIESTS'
        hero_property['HP'] = random.randint(100,2000)
        hero_property['MP'] = random.randint(10,100)
        hero_property['Attack'] = random.randint(10,150)
        hero_property['Armor'] = random.randint(0,50)
        hero_property['costMP'] = 5
        hero_property['Magicskill'] = '生命汲取'
        hero_property['diemessage'] = '死亡是另一种开始...'
    
    hero_property['maxHP'] = hero_property['HP']
    hero_property['maxMP'] = hero_property['MP']
    
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
    8，treant,boss2, 血极其厚，攻击力中等
    9，kid, 十分随缘的boss3(有几率一击必杀主角)
    10, rock, 血厚无攻击力
    """

    
    if enemy_kind == 1:
        enemy_data = {'name':'snake', 'HP':random.randint(100,300), 'MP':random.randint(0,10), \
                               'Attack':random.randint(5,15), 'Armor':random.randint(0,10), \
                               'exp':1}
    elif enemy_kind == 2:
        enemy_data = {'name':'wolf', 'HP':random.randint(200,400), 'MP':random.randint(0,50), \
                               'Attack':random.randint(50,70), 'Armor':random.randint(10,20), \
                               'exp':2}
    elif enemy_kind == 3:
        enemy_data = {'name':'eagle', 'HP':random.randint(100,500), 'MP':random.randint(60,90), \
                               'Attack':random.randint(10,40), 'Armor':random.randint(30,40), \
                               'exp':3}
    elif enemy_kind == 4:
        enemy_data = {'name':'zombie', 'HP':random.randint(800,1000), 'MP':random.randint(10,70), \
                               'Attack':random.randint(10,40), 'Armor':random.randint(10,30), \
                               'exp':10}
    elif enemy_kind == 5:
        enemy_data = {'name':'robber', 'HP':random.randint(600,1000), 'MP':random.randint(20,60), \
                               'Attack':random.randint(60,90), 'Armor':random.randint(20,50), \
                               'exp':10}
    elif enemy_kind == 6:
        enemy_data = {'name':'drunkenrobber', 'HP':random.randint(1,2000), 'MP':random.randint(0,200), \
                               'Attack':random.randint(0,100), 'Armor':random.randint(0,60), \
                               'exp':random.randint(0,20)}
    elif enemy_kind == 7:
        enemy_data = {'name':'robberleader', 'HP':random.randint(1000,1200), 'MP':random.randint(200,300), \
                               'Attack':random.randint(80,120), 'Armor':random.randint(50,60), \
                               'exp':30}
    elif enemy_kind == 8:
        enemy_data = {'name':'treant', 'HP':random.randint(5000,7000), 'MP':random.randint(200,600), \
                               'Attack':random.randint(10,30), 'Armor':random.randint(50,80), \
                               'exp':40}
    elif enemy_kind == 9:
        enemy_data = {'name':'kid', 'HP':random.randint(1,10000), 'MP':random.randint(0,600), \
                               'Attack':random.randint(0,200), 'Armor':random.randint(0,90), \
                               'exp':random.randint(10,50)}
    elif enemy_kind == 10:
        enemy_data = {'name':'rock', 'HP':random.randint(900,1300), 'MP':random.randint(0,0), \
                               'Attack':random.randint(0,0), 'Armor':random.randint(40,90), \
                               'exp':1}
    else:
        enemy_data = {'name':'flower', 'HP':random.randint(1,5), 'MP':0, \
                               'Attack':0, 'Armor':0 ,'exp':0}
    return enemy_data