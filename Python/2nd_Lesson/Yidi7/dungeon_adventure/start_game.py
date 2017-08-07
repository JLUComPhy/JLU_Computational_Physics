#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from source.game import *
from source.game_map import *
from source.print_delay import *


if __name__ == '__main__':
  game = Game()
  game.welcome()
  character = game.create_new_character()
  game_map = GameMap(5, 5)
  while True:
    character.move(game_map)
    enemy = game.generate_enemy()
    if enemy:
      while enemy.alive:
        prints(("%s剩余HP：%s/%s\n%s剩余HP：%s/%s\n"
                % (character.name, character.hp, character.fullhp,
                   enemy.name, enemy.hp, enemy.fullhp)))
        character.action(enemy)
        if character.escaped: break
        enemy.action(character)
