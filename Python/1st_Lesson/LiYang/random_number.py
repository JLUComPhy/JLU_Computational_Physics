#!/usr/bin/python 
# -*- coding: UTF-8 -*-

import random
random.seed()

print ("===========猜数游戏===========")

mod_chioce = raw_input("请选择猜数模式(人工／机器)(输入:'p' or 'm'): ")

if 'p' == mod_chioce or 'P' == mod_chioce:
    #人为猜测模块
    actual_number = random.randint(0,1024)

    for cir in range(9,-1,-1):
        input_number = (int)(raw_input("请输入您猜的数:"))
        if actual_number == input_number:
            print ("恭喜您猜对啦!")
            break
        elif actual_number > input_number:
            print ("小了!")
            print ("---您还有%d次机会---" %(cir))
        else:
            print ("大了!")
            print ("---您还有%d次机会---" %(cir))


else:
    #二分法猜测
    
    guass_time = 100000000

    time_right = 0
    for try_cir in range(guass_time):
        actual_number = random.randint(0,1024)
        
        print (1.0 * try_cir / guass_time)

        min_lim = 0
        max_lim = 1024
 
        for cir in range(10):
            guass_number = (min_lim + max_lim) / 2
            if guass_number == actual_number:
                time_right += 1
                break
            elif guass_number > actual_number:
                max_lim = guass_number
            else:
                min_lim = guass_number

    possible_right = 1.0 * time_right / guass_number

    print ('二分法猜对的概率为:%d' %(time_right))