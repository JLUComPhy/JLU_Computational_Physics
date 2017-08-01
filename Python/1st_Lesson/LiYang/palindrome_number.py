#!/usr/bin/python
# -*- coding: UTF-8 -*-

jud_num = (int)(raw_input('请输入要判断的数:'))

tem_num = jud_num 
inv_num = 0
while tem_num:
    inv_num = inv_num * 10 + tem_num % 10
    tem_num = tem_num / 10

if inv_num == jud_num:
    print ('%d 是  回文数' %(jud_num))
else:
    print ("%d 不是 回文数" %(jud_num))