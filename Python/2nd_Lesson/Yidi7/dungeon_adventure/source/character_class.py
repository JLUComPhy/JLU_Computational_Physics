#!/usr/bin/python2.7'
# -*- coding: utf-8 -*-
# 职业列表，用于初始化属性点和魔法列表


from creature import *
from magic_list import *


class Warrior(Hero):

  def __init__(self, name):
    super(Warrior, self).__init__(name)
    self.strength = 12
    self.intelligence = 3
    self.constitution = 12
    self.luck = 10
    self.hp = 20
    # self.hp = 0
    self.mp = 5
    self.magic_list = warrior_magic_list


class Mage(Hero):

  def __init__(self, name):
    super(Mage, self).__init__(name)
    self.strength = 5
    self.intelligence = 15
    self.constitution = 7
    self.luck = 10
    self.hp = 15
    self.mp = 20
    self.magic_list = mage_magic_list
