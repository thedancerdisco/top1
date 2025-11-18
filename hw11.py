# #практическое задание 5
# import math
# from typing import Tuple
# def solve(a: int, b: int, c: int)->tuple[float, float]:
#     #вычисляем дискриминант
#     d: int = b**2 - 4*a*c
#     if d<0:
#         print("действительных корней нет")
#         return
#     x_1: float = (-b+math.sqrt(d))/(2*a)
#     x_2: float = (-b-math.sqrt(d))/(2*a)


#     return x_1, x_2
# print(*solve(1,4,3))


#домашнее задание
dic:dict = {}
title: str = ""

def  make_report(title:str, **sections: dict[str,int])->dict[str, int]:
    s:int = 0
    title = input("введи название отчета ")
    while True:
        key = input('введи название секции ')
        if not key:
            break
        dic[key] = int(input("число по секции "))
    dic["общая сумма"] = sum( dic.values())
    print(f"===Отчет: {title}===")
    for key, val in dic.items():
        print(f"{key}:   {val}")

make_report(title, sections=dic)
