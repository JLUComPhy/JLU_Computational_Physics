# -*- coding: utf-8 -*-
import time
def ck_state(Player,state,pl_hp):
	if state == 'poisoning':
		pl_hp -= int(pl_hp*0.1) + 1
		print('由于中毒，'+Player.name+'减少'+str(int(pl_hp*0.1) + 1)+'的hp')
	return pl_hp	
	
def sting(Player):
	return 'poisioning'
					
def bet(Player,Enemy):
	state = Player.state
	em_hp = Enemy.hp 
	pl_hp = 30
	em_dem = Player.atk - Enemy.de
	pl_dem = Enemy.atk - Player.de
	while True:
		com_tmpt = raw_input('choose your action : a(attack), s(skill),i(items),e(escape)')
		if com_tmpt == 'a':
			em_hp -= em_dem
			time.sleep(0.5)
			print(Player.name+'攻击，'+Enemy.name+'损失了'+str(em_dem)+'hp')
			time.sleep(0.5)
			if em_hp > 0:
				if Enemy.skill == []:
					pl_hp -= pl_dem
					print(Enemy.name+'普通攻击，'+Player.name+'受到'+str(pl_dem)+'点伤害')
				else:
					at_index = random.uniform(0,1)
					if at_index >0.3:
						pl_hp -= pl_dem
						print(Enemy.name+'普通攻击，'+Player.name+'受到'+str(pl_dem)+'点伤害')	
					else:
						pl_hp -= pl_dem
						print(Enemy.name+'普通攻击，'+Player.name+'受到'+str(pl_dem)+'点伤害')
						time.sleep(0.5)
						print(Player.name+'中毒了')
						state = 'poisoning'
			else:
				print(Enemy.name+'被打倒了，获得'+str(Enemy.exp)+'点经验 ,'+str(Enemy.money)+'$到手了！！')	 
				time.sleep(0.5)
				break
		elif com_tmpt == 's':
			time.sleep(0.5)
			pass
		elif com_tmpt == 'i':
			time.sleep(0.5)
			pass
		elif com_tmpt	== 'e':
			time.sleep(0.5)
			print(Player.name+'逃跑了......')
			break
		pl_hp=ck_state(Player,state,pl_hp)
			
		if pl_hp <= 0:
			print('Game over!')
			state = 'dead'
			break
		time.sleep(0.5)	
		print('')
	return state 
	
	
import random
def bet_enc(Player):
	a=random.uniform(0,1)
	enc_index = ''
	if a <= 0.3:#难度系数：遇敌概率0.3
		b = random.randint(0,2)
		enc_index = b
	return enc_index		
	
					
