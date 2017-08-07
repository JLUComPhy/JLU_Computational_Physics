#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from creature import Enemy

# Enemy(name, hp, attack, luck, odd)
goblin = Enemy('哥布林', 20, 3, 4, 0.15)
wolf   = Enemy('野狼', 15, 5, 6, 0.1)
spider = Enemy('巨型蜘蛛', 30, 6, 8, 0.05)

mon_list = [goblin, wolf, spider]
