#!/usr/bin/python2.7
# -*- coding: utf-8 -*-


from random import *
import time

###############直接复制以下代码即可#################
#Getch每次读取一个字符作为移动和战斗的指令
class _Getch:
    """Gets a single character from standard input.  Does not echo to the screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()
###############################################################


def prints(string): # 延时输出
  time.sleep(0.4)
  print string
  time.sleep(0.4)


def printss(string): # 延时输出
  print string
  time.sleep(0.1)

  
def move(): # 移动函数
  global getch
  move_success = False
  while not move_success:
    print "%s" % char_position
    print "移动 >",
    direction = getch()
    position = char_position[:]

    if direction == 'w':
      position[1] += 1
    elif direction == 'a':
      position[0] -= 1
    elif direction == 's':
      position[1] -= 1
    elif direction == 'd':
      position[0] += 1
    else:
      prints("按w/a/s/d移动")
      continue

    if not check_boundary(position):  # 人物抵达地图边界
      prints("你向前走去，触摸到了冰冷的墙壁")
    else:
      move_success = True
      char_position[:] = position
     # print "%s" % char_position
     # print "You are now on %s" % char_position


# 检查是否抵达边界
def check_boundary(position):
  if ((position[0] > boundary[0] or position[1] > boundary[1] or
       position[0] < 1 or position[1] < 1)):
    return False
  else:
    return True


def enemy_encounter(): 
  goblin = {'name': '哥布林', 'HP': 20, 'attack': 2, 'luck': 4}
  wolf = {'name': '野狼', 'HP': 15, 'attack': 5, 'luck': 6}
  spider = {'name': '巨型蜘蛛', 'HP': 30, 'attack': 6, 'luck': 8}
  dice = random()
  if dice < 0.2:
    return {'encounter': True, 'who': goblin}
  if dice >= 0.2 and dice < 0.3:
    return {'encounter': True, 'who': wolf}
  if dice >= 0.3 and dice < 0.35:
    return {'encounter': True, 'who': spider}
  else:
    return {'encounter': False}


def fight(enemy_dict):
  global getch
  global character_fullhp
  enemy = enemy_dict.copy()
  enemy_fullhp = enemy['HP']
  print "\n########################################"
  prints("你遇到了一只%s!" % enemy['name'])
  while character['HP'] > 0 or enemy['HP'] > 0:
    prints(("你剩余HP：%s/%s\n%s剩余HP：%s/%s\n"
            % (character['HP'], character_fullhp,
               enemy['name'], enemy['HP'], enemy_fullhp)))
    prints("你想要做什么?\nA: 战斗; B: 逃跑")
    # fight_option = raw_input('>')
    fight_option = getch()
    
    if fight_option == 'A' or fight_option == 'a':
      print "你挥剑向%s砍去" % enemy['name']
      character_damage = char_damage(character)
      prints("你对%s造成了%s点伤害"
             % (enemy['name'], character_damage))
      enemy['HP'] -= character_damage
      if enemy['HP'] <= 0:
        return 'win'
    elif fight_option == 'B' or fight_option == 'b':
      print "你脚下生风，准备开溜"
      dice = random()
      if dice < (character['luck'] - enemy['luck'])* 0.1:
        return 'escape'
      prints("%s发现了你的意图，挡在了你的面前" % enemy['name'])
    else:
      print "请按a或者b进行行动\n"
      continue

    enemy_damage = char_damage(enemy)
    prints("%s对你造成了%s点伤害" % (enemy['name'], enemy_damage))
    character['HP'] -= enemy_damage
    if character['HP'] <= 0:
      prints("你挂了！")
      return 'lose'


def char_damage(char):  # 判断角色伤害
  dice = random()
  damage = char['attack'] + int(char['luck'] * dice * 0.5)
  return damage


def welcome():
  printss("                                                                            ")
  printss("                                                                            ")
  printss("              #               #                                             ")
  printss("           #  #         ############     #############     ###      #       ")
  printss("      #  ##########     #  #  #    #     #############     ###    #   #     ")
  printss("     ###   #  #   #       ########       #############     # #   #     #    ")
  printss("      #    #  #   #      #    #             #######        ###  # ##### #   ")
  printss("      #    #    ###      ##########         #######        #      # # #     ")
  printss("     ###   #                  #             #######        #       # #      ")
  printss("           ########           #             #######        #     #######    ")
  printss("                                                                            ")
  printss("                                                                            ")
  printss("                                                                            ")
  printss("                                                                            ")
  printss("                                按回车键继续                                 ")
  printss("                                                                            ")
  printss("                                                                            ")
  printss("                                                                            ")
  printss("                                                                            ")
  raw_input()
  raw_input('"我在哪里?", 你从昏睡中醒来, 感到头部一阵剧痛. [回车]')
  raw_input('你站起身环顾四周, 无边的黑暗中闪烁着几片微弱的火光. [回车]')
  raw_input('你拿起地上一把生锈的铁剑, 决心一探究竟. [回车]')


if __name__ == "__main__":
  character = {'HP': 40, 'attack': 8, 'luck': 10}
  character_fullhp = character['HP']
  char_position = [1, 1]
  boundary = (5, 5)
  map_exit = [randint(2, boundary[0]), randint(2, boundary[1])]
  #print map_exit
  getch = _Getch()
  welcome()
  while True:
    move()
    if char_position == map_exit:
      prints("你发现了地牢的出口, 成功逃出地牢! 大吉大利, 今晚吃鸡!")
      exit(0)

    enemy = enemy_encounter()
    if enemy['encounter']:
      fight_result = fight(enemy['who'])
      if fight_result == "win":
        prints("战斗胜利！剩余%s点HP" % character['HP'])
      elif fight_result == "lose":
        prints("胜败乃兵家常事，大侠请重新来过")
        exit(0)
      elif fight_result == "escape":
        prints("你借着地牢内阴暗的光线逃离了敌人的魔爪")

