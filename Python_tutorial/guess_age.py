#!/usr/bin/env python3.7
# -*- coding:utf-8 # -*- 
"""

@File    : guess_age.py
@Author  : NIE ZIYU
@Email   : ziyuwill@gmail.com
@IDE     : PyCharm 
@Create_Time : 2019-01-18 15:33

"""


real_age = 33
guess_age = int(input("Aeg:"))

if real_age > guess_age:
    print("猜小了")
elif real_age < guess_age:
    print("猜到了")
elif real_age == guess_age:
    print("猜对了")
