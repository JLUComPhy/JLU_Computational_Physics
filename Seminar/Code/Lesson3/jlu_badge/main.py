#!/usr/bin/python
# -*- coding:UTF-8 -*-
from scipy.misc import imread
import numpy as np

import random

jlu_badge = imread('jlu_badge_without_words.png')

real_pix_color_num = 0
monte_carlo_pix_color_num = 0

for colunm in range(jlu_badge.shape[1]):
  for row in range(jlu_badge.shape[2]):
    #print jlu_badge[colum, row]
   
    white_pix = np.array([255, 255, 255, 255])
    if (jlu_badge[row, colunm] != white_pix).any():
      real_pix_color_num += 1

real_pic_ratio = real_pix_color_num*1.0/(jlu_badge.shape[1]*jlu_badge.shape[2])
print str(real_pix_color_num)+'/'+str(jlu_badge.shape[1]*jlu_badge.shape[2])+'='\
     +str(real_pic_ratio)
  
max_pick = 10
for pick in range(max_pick):
  random_row = random.randint(0, jlu_badge.shape[2]-1)
  random_colunm = random.randint(0, jlu_badge.shape[1]-1)
  #print(pick*1.0/max_pick) 

  if (jlu_badge[random_row, random_colunm] != white_pix).any():
    monte_carlo_pix_color_num += 1

monte_carlo_pic_ratio = monte_carlo_pix_color_num*1.0/(max_pick)
print str(monte_carlo_pix_color_num)+'/'+str(max_pick)+'='\
    +str(monte_carlo_pic_ratio)

print str(max_pick)+' ==dif==>'+str((real_pic_ratio-monte_carlo_pic_ratio)/real_pic_ratio * 100)+'%' 
  