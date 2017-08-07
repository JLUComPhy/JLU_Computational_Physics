#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# 魔法列表，同样的功能也可以通过字典实现，但是用类实现便于之后根据不同魔法的属性和附加效果再增加代码


class Magic(object):

  def __init__(self, name, cost, damage):
    self.name = name
    self.cost = cost
    self.damage = damage


# 通过实例化增加魔法，之后再添加到特定职业的魔法列表里
fireball = Magic('火球术', 3, 10)
arcane_missiles = Magic('奥术飞弹', 5, 15)
blizzard = Magic('暴风雪', 10, 25)

warrior_magic_list = []
mage_magic_list = [fireball, arcane_missiles, blizzard]
