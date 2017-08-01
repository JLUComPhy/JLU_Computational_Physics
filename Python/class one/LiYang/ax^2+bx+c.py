#!/usr/bin/python
# -*- coding: UTF-8 -*-
print("=================解一元二次方程====================")
print("ax^2 + bx + c = 0")
print("请输入相关系数:")

a = float(raw_input("a = "))   #a = input('a = ')
b = input('b = ')
c = input('c = ')

print("-------------------------------------------------")
print("%r*x^2 + %r*x + %r = 0" %(a,b,c))
print("-------------------------------------------------")
print("解得:")

delta = b**2 - 4*a*c  

if delta < 0:
    delta = - delta
    jud_conj = complex(0,1) 
else:
    jud_conj = 1 

solve_fir = - 1.0 * b / (2*a)
solve_sec = (delta**0.5) / (2*a)

#================one_solution==============
x1 = solve_fir + solve_sec * jud_conj
x2 = solve_fir - solve_sec * jud_conj

print ("x1 = %s" %x1)
print ("x2 = %r" %x2)

#只能在支持复数运算的语言上应用
#==========================================


#=================another_solution========
if jud_conj == 1:
    print ("x1 = %f" %(solve_fir+solve_sec))
    print ("x2 = %f" %(solve_fir+solve_sec))
else:
     print ("x1 = %f + %fi" %(solve_fir, solve_sec))
     print ("x2 = %f - %fi" %(solve_fir, solve_sec))
     
#在解为纯虚数时有问题,且可移植性差,不能作为模块处理
#=========================================
print("==================================================")
