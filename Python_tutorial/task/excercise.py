#!/usr/bin/env python3.7
# -*- coding:utf-8 # -*- 
"""

@File    : excercise.py
@Author  : NIE ZIYU
@Email   : ziyuwill@gmail.com
@IDE     : PyCharm 
@Create_Time : 2019-01-18 14:53

"""
# name = input("Name:")
# gender = input("Gender:")
# age = int(input("Age:"))
#
# if gender == "f":
#     if age < 38:
# #         print("我喜欢女生")
# #     else:
# #         print("姐弟恋也很好")
# # else:
# #     print("一起来搞基")
#
# name = input("Name:")
# gender = input("Gender:")
# age = int(input("Age:"))
#
# if gender == "f" and age < 28:
#     print("i love girls")
# else:
#     print("i love old woman")

score = float(input("your score:"))

if score >100:
    print("成绩最高为100")
elif score > 90 and score < 100:
    print("你的成绩是A")
elif score >80 and score < 89:
    print("你的成绩是B")
elif score > 60 and score <79:
    print("你的成绩是C")
elif score >40 and score <59:
    print("你的成绩是D")
else:
    print("你的成绩是E")

