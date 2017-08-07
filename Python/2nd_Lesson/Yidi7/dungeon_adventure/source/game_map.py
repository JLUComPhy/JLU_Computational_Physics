#!/usr/bin/python2.7'
# -*- coding: utf-8 -*-

from random import *


class GameMap(object):

  def __init__(self, boundary_x, boundary_y):
    self.boundary = [boundary_x, boundary_y]
    self.map_exit = [randint(2, self.boundary[0]),
                      randint(2, self.boundary[1])]
