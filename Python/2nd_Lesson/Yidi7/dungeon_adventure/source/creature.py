#!/usr/bin/python2.7'
# -*- coding: utf-8 -*-
# 此文档下的类为游戏中的生物，包括主角和敌对生物

from print_delay import *
from random import *
from game_map import *
from getchar import _Getch


class Creature(object):  

  def __init__(self):
    self.name = None
    self.strength = None
    self.intelligence = None
    self.constitution = None
    self.luck = None
    self.attack = None
    self.hp = None
    self.fullhp = None
    self.mp = None
    self.fullmp = None
    self.damage = None
    self.alive = True

  def fight(self, opponent):  # 战斗函数 
    dice = random()
    self.damage = self.attack + int(self.luck * dice * 0.5)
    opponent.hp -= self.damage
    # setattr(opponent, opponent.hp, opponent.hp)
    prints("%s对%s造成了%s点伤害" % (self.name, opponent.name, self.damage))
    if opponent.hp <= 0:  # 判断敌人是否被击败
      opponent.alive = False


class Hero(Creature):  # 主角类

  def __init__(self, name):
    super(Hero, self).__init__()
    self.name = name
    self.char_position = [1, 1]
    self.escaped = True
    self.magic_list = None

  def move(self, GameMap):  # 移动函数
    getch = _Getch()
    move_success = False
    while not move_success:
      print "位置：%s" % self.char_position
      print "移动 >",
      direction = getch()
      position = self.char_position[:]

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

      if not self.check_boundary(position, GameMap):  # 人物抵达地图边界
        print "你向前走去，触摸到了冰冷的墙壁"
      else:
        move_success = True
        self.char_position[:] = position

      # print GameMap.map_exit
      if self.char_position == GameMap.map_exit:   
        prints("你发现了地牢的出口, 成功逃出地牢! 大吉大利, 今晚吃鸡!")
        exit(0)

  def check_boundary(self, position, GameMap):
    if ((position[0] > GameMap.boundary[0] or
         position[1] > GameMap.boundary[1] or
         position[0] < 1 or position[1] < 1)):
      return False
    else:
      return True

  def action(self, opponent):  # 行动函数
    if not self.alive:  # 判断自身是否具有行动能力
      prints("你挂了！")
      prints("胜败乃兵家常事，大侠请重新来过")
      exit(0)

    getch = _Getch()
    prints("你想要做什么?\nA: 攻击; B: 魔法; C: 逃跑")
    action_option = getch()
    self.escaped = False
    if action_option == 'A' or action_option == 'a':
      self.fight(opponent)
    elif action_option == 'B' or action_option == 'b':
      self.choose_magic(opponent)
    elif action_option == 'C' or action_option == 'c':
      self.escape(opponent)
    else:
      print "不存在的操作！"
      self.action(opponent)

  def fight(self, opponent):
    self.attack = self.strength  # 普通攻击
    super(Hero, self).fight(opponent)

  def choose_magic(self, opponent):
    if not self.magic_list:
      print "没有可用的魔法"
      self.action(opponent)
    else:
      print "剩余MP：%d" % self.mp
      print "可用的魔法列表："
      for i in range(len(self.magic_list)):
        print ("%d. %s(%dmp)"
               % (i+1, self.magic_list[i].name, self.magic_list[i].cost))
      print "使用魔法 > ",
      getch = _Getch()
      magic_option = getch()
      print magic_option
      for j in range(len(self.magic_list)):
        if magic_option == str(j+1):  # 判断是否存在输入的魔法
          if self.magic_list[j].cost > self.mp:
            print "魔法值不足！"
            self.choose_magic(opponent)
          else:
            self.cast_magic(opponent, self.magic_list[j])
          break
      else:
        print "你的记忆中没有这个魔法\n"
        self.action(opponent)

  def cast_magic(self, opponent, magic):
    # 可以选择魔法的属性，改变计算公式，如改智力为幸运等
    self.attack = magic.damage + self.intelligence
    self.mp -= magic.cost
    prints("使用魔法：%s, 剩余MP：%d/%d" % (magic.name, self.mp, self.fullmp))
    super(Hero, self).fight(opponent)

  def escape(self, opponent):
    dice = random()
    print "你脚下生风，准备开溜"
    if dice < (self.luck - opponent.luck) * 0.1:
      self.escaped = True
      prints("你借着地牢内阴暗的光线逃离了敌人的魔爪")
    else:
      prints("%s发现了你的意图，挡在了你的面前" % opponent.name)


class Enemy(Creature):

  def __init__(self, name, hp, attack, luck, odd):
    super(Enemy, self).__init__()
    self.name = name
    self.hp = hp
    self.fullhp = hp
    self.attack = attack
    self.luck = luck
    self.odd = odd

  def reset(self):
    self.hp = self.fullhp
    self.alive = True

  def action(self, opponent):
    if self.alive:
      self.fight(opponent)
    else:
      prints("战斗胜利！\n")
