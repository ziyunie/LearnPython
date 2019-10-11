#!/usr/bin/env python3.7
# -*- coding:utf-8 # -*- 
"""

@File    : guess_age_2.0.py
@Author  : NIE ZIYU
@Email   : ziyuwill@gmail.com
@IDE     : PyCharm 
@Create_Time : 2019-01-21 15:36

"""


count = 0

real_age = 33

while count < 3:

    guess_age = int(input("Aeg:"))

    if real_age > guess_age:
        print("猜小了")
    elif real_age < guess_age:
         print("猜大了")
    else:
         print("猜对了")
         break
    count += 1