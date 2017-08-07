#!/usr/bin/python2.7'
# -*- coding: utf-8 -*-

from random import *
from monster_list import *
from print_delay import *
from character_class import *


class Game(object):

  def create_new_character(self):
    print "你逐渐回想起了自己的名字:"
    char_name = raw_input('姓名 > ')
    print "你想起自己其实是一名：（战士/法师）"
    while True:
      char_class = raw_input('职业 > ')
      if char_class == '战士':
        character = Warrior(char_name)
        break
      elif char_class == '法师':
        character = Mage(char_name)
        break
      else:
        print "你好像记错了，你知道自己其实是一名：（战士/法师）"

    while True:
      print ("\n你的初始点数为: 力量%s 智力%s 体质%s 幸运%s"
             % (character.strength, character.intelligence,
                character.constitution, character.luck))
      extra_attr = 6
      print "你可以分配的初始点数为%s\n" % extra_attr
      print "力量决定普通攻击的伤害"
      print "智力决定魔法值和法术伤害"
      print "体质决定生命值"
      print "幸运是个神秘的属性\n"
      while not extra_attr == 0:
        extra_attr = 6
        extra_strength = int(raw_input("分配几点给力量？（%s剩余) " % extra_attr))
        extra_attr -= extra_strength
        extra_intelligence = int(raw_input("分配几点给智力？（%s剩余）" % extra_attr))
        extra_attr -= extra_intelligence
        extra_constitution = int(raw_input("分配几点给体力？（%s剩余）" % extra_attr))
        extra_attr -= extra_constitution
        extra_luck = int(raw_input("分配几点给幸运？（%s剩余）" % extra_attr))
        extra_attr -= extra_luck
        if not extra_attr == 0:
          print "分配点数超出或有剩余，请重新分配\n"
      print "是否确定该分配方案？输入r可重新分配，其他则确认分配"
      if not raw_input('>') == 'r': break

    character.strength += extra_strength
    character.intelligence += extra_intelligence
    character.constitution += extra_constitution
    character.luck += extra_constitution
    character.hp += character.constitution * 2
    character.fullhp = character.hp
    character.mp += character.intelligence
    character.fullmp = character.mp
    return character

  def generate_enemy(self):
    dice = random()
    odd = 0
    for monster in mon_list:
      odd += monster.odd
      # print dice, odd
      if dice <= odd:
        print "\n########################################"
        prints("你遇到了一只%s!" % monster.name)
        monster.reset()
        return monster

  def welcome(self):
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
    raw_input('你环顾四周, 无边的黑暗中闪烁着几片微弱的火光. [回车]')
    raw_input('你站起身, 决心一探究竟. [回车]')
