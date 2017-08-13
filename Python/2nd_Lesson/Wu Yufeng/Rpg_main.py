#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
class Player:
	def __init__(self, name, hp, mp, atk, de,skill,exp,level,items,position,state,money):
		self.name = name
		self.hp = hp
		self.mp = mp
		self.atk = atk
		self.de = de
		self.skill = skill
		self.exp = exp
		self.level = level
		self.items = items
		self.position = position
		self.state = state
		self.money = money
	
class Enemy:
	
	def __init__(self,name,hp,mp,atk,de,exp,skill,money):
		self.name = name
		self.hp = hp
		self.mp = mp
		self.atk = atk
		self.de = de
		self.exp = exp
		self.skill = skill
		self.money = money
		
Goblin = Enemy('Gobllin',6,0,7,0,5,[],10)
LegEater = Enemy('LegEater',6,0,5,0,5,[],10)
QueenBee = Enemy('QueenBee',6,0,9,0,5,['sting'],10)
Enemy_list = [Goblin,LegEater,QueenBee]
#----------------------------------------------------------------------

#start menu
import time
import copy
from Rpg_stage import *
import random 

from Rpg_betsys import bet
from Rpg_betsys import bet_enc
from Rpg_move import mov  

print('Welocome to Final Fantasy!!!')	
time.sleep(0.4)
raw_input('enter any key to start ')

time.sleep(0.4)						
#创建人物			 
Player1 = Player(raw_input('Please enname your warrior : '), 30, 5, 4, 0, [], 0, 1, [], [0, 0], '', 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
<<<<<<< HEAD:Python/2nd_Lesson/Wu Yufeng/Rpg_main.py
scipt1(Player1.name)
=======
Rpg_stage.scipt1(Player1.name)
>>>>>>> 10c68c86c2c8e3f835f6425f67f78a0a472b2879:Python/2nd_Lesson/Wu Yufeng/Rpg_main.py

while True:
	pos_temp0 = copy.deepcopy(Player1.position)
	pos_temp1, Player1.items, Player1.money = copy.deepcopy(mov(Player1))
	if pos_temp0 != pos_temp1:
		index = bet_enc(Player1)
		if index != '':
			print(Enemy_list[index].name+'出现了！！')
			time.sleep(1)
			Player1.state = bet(Player1,Enemy_list[index])
			time.sleep(1)
			Player1.exp += Enemy_list[index].exp
			Player1.money += Enemy_list[index].money

	    
