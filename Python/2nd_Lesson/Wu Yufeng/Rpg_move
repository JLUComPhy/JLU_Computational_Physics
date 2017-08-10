# -*- coding: utf-8 -*-
class item:
	def __init__(self,name,price,effect,abbreviation):
		self.name = name
		self.price = price
		self.effect = effect
		self.abb = abbreviation
		
Potion = item('Potion',10,'healing','p')		
Antidote = item('Antidote',30,'detoxify','a')
item_list = [Potion,Antidote]
#----------------------------------------------------------------------

def detoxify(Player):
	if Player.state == 'posioning':
		Player.state = ''
	return Player.state	
#----------------------------------------------------------------------
def shop(Player,item_list):
	choice = raw_input('请选择你要购买的商品：p(Potion 10$) a(Antidote 20$) ')
	for i in item_list:
		if choice == i.abb:
			if Player.money < i.price:
				print('你没有足够的金币，无法购买！')
			else:
				print('成功购买'+i.name+'，你还有'+str(Player.money - i.price)+'$')
				Player.items.append(i.name)
				Player.money -= i.price
	return Player.items,Player.money
		
def ues_item(Player):
	for i in Player.items:
		print(i.abb+':'+i.name)
	choice = raw_input('请选择要使用的物品：')
	if choice == 'p':
		pass
	elif choice == 'a':
		Player.state = detoxify(Player)

#--------------------------------------------------------------------				
def detail(Player):
	print('name: '+Player.name,'hp: '+str(Player.hp),'mp: ',Player.mp,'atk: ',Player.atk,'de: ',Player.de,'skill: ',Player.skill,'exp: ',Player.exp,'level: ',Player.level,'items: ',Player.items,'Position : ',Player.position,'State : ',Player.state,'Money :',Player.money)		

				
#-------------------------------------------------------------------												
def mov(Player):
	sence_size = [30,30]
	pos_temp = Player.position
	tape = raw_input('>>>：')
	if tape == 'w':
		if Player.position[1] < sence_size[1]:
			pos_temp[1] += 1
			print(Player.name+'向北前进了一步')
		else: 
			print('已到达北边缘')
	elif tape == 's':
		if Player.position[1] > -1*sence_size[1]:
			pos_temp[1] += -1
			print(Player.name+'向南前进了一步')
		else: 
			print('已到达南边缘')	
	elif tape == 'a':
		if Player.position[0] > -1*sence_size[0]:
			pos_temp[0] += -1	
			print(Player.name+'向西前进了一步')
		else: 
			print('已到达西边缘')	
	elif tape == 'd':
		if Player.position[0] < sence_size[0]:
			pos_temp[0] += 1
			print(Player.name+'向东前进了一步')
		else: 
			print('已到达东边缘')
	elif tape == 'detail':
		detail(Player)	
	elif tape == 'shop':
		Player.items,Player.money = shop(Player,item_list)
	elif tape == 'item':
		Player = ues_item(Player)			
	return pos_temp,Player.items,Player.money
	
