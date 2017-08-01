#!/usr/bin/python
# -*- coding: UTF-8 -*-

#2 3 5 7 11

whichone = int(raw_input("请输入要求的质数序号(大于5的整数):"))

count = 4
number = 9
while count < whichone:
    max_factor = int(number**0.5)
    for factor in range(2,max_factor+1):
        if number%factor == 0:  #一旦被整除，则一定不是质数，跳出循环
            break
        elif factor != (max_factor):              #如果不被整除，则继续判断
            continue
        else:
            count += 1         #如果一直到最后一个，都不被整除，则该数是质数
            print("No.%d ==> Val.%d"%(count, number))
    number += 1